import pandas as pd
import numpy as np
with open("C:/Users/Shayla/Desktop/result2010.txt", "r",encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
import nltk
table = {ord(f):ord(t) for f,t in zip(
    u'，。！？【】（）％＃＠＆１２３４５６７８９０’',
    u',.!?[]()%#@&1234567890\'')}
t = u'中国，中文‘也好，标点符号！你好？１２３４５＠＃【】+=-（）’'
data1 = data.translate(table)
#大小写转换
data2=data1.lower()
#print(data2)
#分句
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
data3=tokenizer.tokenize(data2)
#print(data3)
#替换‘ve等
import nltk
from replacers import RegexpReplacer
replacer= RegexpReplacer()
data4=[]
for i in range(0,len(data3)):
    data4.append(replacer.replace(data3[i]))
#print(data4)

#分词
data5=[]
for j in range(0,len(data4)):
    data5.append(nltk.word_tokenize(data4[j]))
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
#print(lemmatizer.lemmatize('less'))
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
print(len(data7))
#去停止词
data8=[]
from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
for review in data7:
    new_review = []
    new_review=[word for word in review if word not in stops]
    data8.append(new_review)
#print(data8)
#去除数字
data9=[]
from string import digits
for review1 in data8:
    new_review=[]
    new_review=list(filter(lambda x: not str(x).isdigit(), review1))
    data9.append(new_review)
print(data9)
