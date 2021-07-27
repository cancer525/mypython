# 部分参考了别的博主，不过链接忘记了
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img_path = '1.png'
image = Image.open(img_path)

# 要提取的主要颜色数量
num_colors = 5
small_image = image.resize((80, 80))
result = small_image.convert('P', palette=Image.ADAPTIVE, colors=20)
result = result.convert('RGBA')
main_colors = result.getcolors()

col_extract = []
# 显示提取的主要颜色
for count, col in main_colors:
    # print([col[i]/255 for i in range(3)])#RGB转RGBA，可输出RGBA色号
    col_extract.append([col[i] / 255 for i in range(3)])

# 使用提取的颜色绘制条形图
plt.figure(dpi=150)
plt.bar(range(len(col_extract)), np.ones(len(col_extract)), color=(col_extract))
plt.xticks(range(len(col_extract)), (range(len(col_extract))))
plt.show()

from PIL import Image, ImageDraw, ImageFont


def get_dominant_colors(infile):
    image = Image.open(infile)


    result = image.convert(
        "P", palette=Image.ADAPTIVE, colors=10
    )

    # 10个主要颜色的图像

    # 找到主要的颜色
    palette = result.getpalette()
    color_counts = sorted(result.getcolors(), reverse=True)
    colors = list()

    for i in range(10):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index * 3: palette_index * 3 + 3]
        colors.append(tuple(dominant_color))

    # print(colors)
    return colors
color = get_dominant_colors(img_path)
print(color)