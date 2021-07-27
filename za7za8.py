import numpy as np
import nltk
data1=['today is very admire.','today is more abuse.','today is more abuse and very admire.','today is none admire']

#分词
data5=[]
for j in range(0,len(data1)):
    data5.append(nltk.word_tokenize(data1[j]))
#print(data5)
#词形还原
from nltk import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
data6=[]
for n in data5:
    new_n=[]
    for nn in n:
        new_nn=lemmatizer.lemmatize(nn)
        new_n.append(new_nn)
    data6.append(new_n)
#print(data6)
#检验情感词典程度级别副词

#去标点符号
import re
import string
x=re.compile('[%s]' % re.escape(string.punctuation))
data7 = []
for review in data6:
    new_review = []
    for token in review:
        new_token = x.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    data7.append(new_review)

#载入情感词典
posdict = (open('C:/Users/Shayla/Desktop/毕业论文/观点文件/sentiment/posdict.txt', 'r')).read()
negdict = (open('C:/Users/Shayla/Desktop/毕业论文/观点文件/sentiment/negdict.txt', 'r')).read()
mostdict = (open('C:/Users/Shayla/Desktop/毕业论文/观点文件/sentiment/mostdict.txt', 'r')).read()
verydict = (open('C:/Users/Shayla/Desktop/毕业论文/观点文件/sentiment/verydict.txt', 'r')).read()
moredict = (open('C:/Users/Shayla/Desktop/毕业论文/观点文件/sentiment/moredict.txt', 'r')).read()
ishdict = (open('C:/Users/Shayla/Desktop/毕业论文/观点文件/sentiment/ishdict.txt', 'r')).read()
insufficientdict = (open('C:/Users/Shayla/Desktop/毕业论文/观点文件/sentiment/insufficentdict.txt', 'r')).read()
inversedict = (open('C:/Users/Shayla/Desktop/毕业论文/观点文件/sentiment/inversedict.txt', 'r')).read()
#4 定义判断奇数偶数的函数。在判断否定词时使用。
def judgeodd(num):
    if (num/2)*2 == num:
        return 'even'
    else:
        return 'odd'
#5情感分值计算主程序。
def sentiment_score_list(dataset):
    count1 = []
    count2 = []
    for m in range(0,len(dataset)):
        segtmp = dataset[m]
        i = 0 #记录扫描到的词的位置
        a = 0 #记录情感词的位置
        poscount = 0 #积极词的第一次分值
        poscount2 = 0 #积极词反转后的分值
        poscount3 = 0 #积极词的最后分值（包括叹号的分值）
        negcount = 0
        negcount2 = 0
        negcount3 = 0
        for word in segtmp:
            if word in posdict:
                poscount += 1
                c = 0
                for w in segtmp[a:i]:
                    if w in mostdict:
                        poscount *= 4.0
                    elif w in verydict:
                        poscount *= 3.0
                    elif w in moredict:
                        poscount *= 2.0
                    elif w in ishdict:
                        poscount /= 2.0
                    elif w in insufficientdict:
                        poscount /= 4.0
                    elif w in inversedict:
                        c += 1

                if judgeodd(c) == 'odd':
                    poscount *= -1.0
                    poscount2 += poscount
                    poscount = 0
                    poscount3 = poscount + poscount2 + poscount3
                    poscount2 = 0
                else:
                    poscount3 = poscount + poscount2 + poscount3
                    poscount = 0
                a = i + 1


            elif word in negdict:
                negcount += 1
                d = 0
                for w in segtmp[a:i]:
                    if w in mostdict:
                        negcount *= 4.0
                    elif w in verydict:
                        negcount *= 3.0
                    elif w in moredict:
                        negcount *= 2.0
                    elif w in ishdict:
                        negcount /= 2.0
                    elif w in insufficientdict:
                        negcount /= 4.0
                    elif w in inversedict:
                        d += 1
                if judgeodd(d) == 'odd':
                    negcount *= -1.0
                    negcount2 += negcount
                    negcount = 0
                    negcount3 = negcount + negcount2 + negcount3
                    negcount2 = 0
                else:
                    negcount3 = negcount + negcount2 + negcount3
                    negcount = 0
                a = i + 1
                d=0
            else:
                poscount3=0


            i +=1

            # #以下是防止出现负数的情况
        pos_count = 0
        neg_count = 0
        if poscount3<0 and negcount3>0:
            neg_count += negcount3 - poscount3
            pos_count = 0
        elif negcount3 < 0 and poscount3 > 0:
            pos_count = poscount3 - negcount3
            neg_count = 0
        elif poscount3 < 0 and negcount3 < 0:
            neg_count = -poscount3
            pos_count = -negcount3
        else:
            pos_count = poscount3
            neg_count = negcount3
            count1.append([pos_count, neg_count])
            count2.append(count1)
            count1 = []
    return count2

#6 计算出所需的积极情感值，消极情感值，积极情感均值，消极情感均值，积极情感方差，消极情感方差。
def sentiment_score(senti_score_list):
    score = []
    for review in senti_score_list:
        score_array = np.array(review)
        Pos = np.sum(score_array[:,0])
        Neg = np.sum(score_array[:,1])
        AvgPos = np.mean(score_array[:,0])
        AvgNeg = np.mean(score_array[:,1])
        StdPos = np.std(score_array[:,0])
        StdNeg = np.std(score_array[:,1])
        score.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    return score
a=sentiment_score_list(data7)
b=sentiment_score(a)
print(a)
