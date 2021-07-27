data="Today climate change is also a problem.Tomorrow will be better.Today climate change is also a problem.Tomorrow climate will be better.Tomorrow will be better.Tomorrow will be better.Tomorrow will be better.Tomorrow will be better.Tomorrow will be better.Climate change.Please click our url:www.hushuo.com/new."
import nltk
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
data1=tokenizer.tokenize(data)
print(data1)
with open("C:/Users/Shayla/Desktop/Shell2016.txt", "r",encoding='UTF-8') as f:  # 打开文件
    data2 = f.read()  # 读取文件
    print(data2)
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
data3=tokenizer.tokenize(data2)
print(data3)
