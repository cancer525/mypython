import pandas as pd
import numpy as np
#去短长句
with open("C:/Users/Shayla/Desktop/毕业论文/时间/2012/Total2012.txt", "r",encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    #print(data)
import nltk

#大小写转换
data2=data.lower()
print(len(data2))
#分句
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
data3=tokenizer.tokenize(data2)
#print(data3)
#替换‘ve等
from replacers import RegexpReplacer
replacer= RegexpReplacer()
data4=[]
for i in range(0,len(data3)):
    data4.append(replacer.replace(data3[i]))
#print(len(data4[0]))
#print(data4[0])


#print(len(data7))
data8=[]
for m in range(0,len(data4)-1):
    if len(data4[m])<20000:
            data8.append(data4[m])
print(len(data8))

outfopen = open("C:/Users/Shayla/Desktop/毕业论文/时间/Total2012.txt", 'w',encoding="utf-8")
for i in range(len(data8)):
    s = str(data8[i]) + ' '
    outfopen.write(s)
outfopen.close()