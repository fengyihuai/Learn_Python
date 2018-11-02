# -*- coding:UTF-8 -*-
# 1、计算已下载天空图片的直方图并可视化；
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(root, file))
        if dirs or (not L):
            for index in range(len(dirs)):
                file_name(os.path.join(root, dirs))
    return L

a = file_name('images/自然风光/天空')
for index in range(len(a)):

    plt.figure(index + 1)
    src = Image.open(a[index])
    r, g, b = src.split()
    ar = np.array(r).flatten()
    plt.hist(ar, bins = 256, density=1, facecolor='r')
    ag = np.array(g).flatten()
    plt.hist(ag, bins=256, density=1, facecolor='g')
    ab = np.array(b).flatten()
    plt.hist(ab, bins=256, density=1, facecolor='b')
plt.show()
print()
# for i in range(len(a)):
#     src =