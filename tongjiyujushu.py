import pandas as pd
import numpy as np
import nltk
from nltk import WordNetLemmatizer
from replacers import RegexpReplacer
import re
import string



with open("C:/Users/Shayla/Desktop/毕业论文/统计字符数2/Eni.txt", "r",encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    print(len(data))
table = {ord(f):ord(t) for f,t in zip(
    u'，。！？【】（）％＃＠＆１２３４５６７８９０’',
    u',.!?[]()%#@&1234567890\'')}
t = u'中国，中文‘也好，标点符号！你好？１２３４５＠＃【】+=-（）’'
data1 = data.translate(table)
#大小写转换
data2=data1.lower()
#print(len(data2))
#print(data2)
#分句
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
data3=tokenizer.tokenize(data2)
print(len(data3))

