import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
numacc=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'累计检测次数')
print(numacc)
x = [1,2,3,4,5]
y = [1,1,1,1,1]
z = numacc['检测次数']
height = np.zeros_like(z)  # 新建全0数组，shape和Z相同，据说是图中底部的位置
width = depth = 0.3
ax.bar3d(x, y,  height, width, depth,z, color='darkblue', shade=False)
plt.show()
