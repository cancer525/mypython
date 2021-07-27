import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
numacc=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'累计检测次数')

x = numacc['月份']
y = 1
z = numacc['检测次数']
# 绘图设置
fig = plt.figure()
ax = fig.gca(projection='3d')  # 三维坐标轴
# X和Y的个数要相同
X = numacc['月份']
Y = [1,1,1,1,1]
Z = np.random.randint(0, 1000, 16)  # 生成16个随机整数
# meshgrid把X和Y变成平方长度，比如原来都是4，经过meshgrid和ravel之后，长度都变成了16，因为网格点是16个
xx, yy = np.meshgrid(X, Y)  # 网格化坐标
X, Y = xx.ravel(), yy.ravel()  # 矩阵扁平化
# 设置柱子属性
height = np.zeros_like(Z)  # 新建全0数组，shape和Z相同，据说是图中底部的位置
width = depth = 0.3  # 柱子的长和宽
# 颜色数组，长度和Z一致
c = ['r'] * len(Z)
# 开始画图，注意本来的顺序是X, Y, Z, width, depth, height，但是那样会导致不能形成柱子，只有柱子顶端薄片，所以Z和height要互换
ax.bar3d(X, Y, height, width, depth, Z, color=c, shade=False)  # width, depth, height
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
