import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D

import hanshu

proapp=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'省公司每月检测缺陷密度')
proapp0=hanshu.zyzh(proapp)
print(proapp0)
fig = plt.figure(5)
ax=fig.add_subplot(1,1,1,projection='3d')     #绘制三维图
x=proapp['org_id']
y=proapp['yue']  #获取x轴数据，y轴数据
z=proapp['rat']   #获取z轴数据
#
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)  #绘制三维图表面
ax.set_xlabel('x-name')     #x轴名称
ax.set_ylabel('y-name')     #y轴名称
ax.set_zlabel('z-name')     #z轴名称
plt.savefig('12.png',dpi=400,bbox_inches='tight')
plt.show()