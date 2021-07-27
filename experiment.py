list1=['abc','c d f','cf ef dg']
list2=['a']
for i in range(0,len(list1)):
    res=[one for one in list1[i] if one in list2]
    print(list1[i])
# 筛选出data_list中所有的dog并保存在new_data_list中
import re

data_list = [['cat_1', 'dog'], ['cat_2 bee'], ['dog_3'], ['cat_3 dog', 'dog cat_3', 'bee'],['bee'],['cat_1']]  # 原列表中既有dog也有cat, 并且无规律
data_list2 = ['bee','dog']
new_data_list = []  # 保存筛选出来dog的列表


#print(len(data5)/len(data3))

for i in range(0,len(data_list)):
    for data in data_list[i]:  # 遍历列表
        if data in data_list2:
            new_data_list.append(data_list[i])
#print(new_data_list)
table = {ord(f):ord(t) for f,t in zip(
    u'，。！？【】（）％＃＠＆１２３４５６７８９０‘',
    u',.!?[]()%#@&1234567890')}
t = u'中国，中文‘也好，标点符号！你好？１２３４５＠＃【】+=-（）’'
t2 = t.translate(table)
print(t2)
print('你好，中故宫‘')