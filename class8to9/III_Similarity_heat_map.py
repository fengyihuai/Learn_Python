# -*- coding:UTF-8 -*-
from matplotlib import pyplot as plt
import numpy as np
from pandas import DataFrame

def plotfuc(idx, col, file):
    # 绘图程序，加载存放系数的文件file
    dfdata = np.loadtxt(file)
    # 对系数reshape到numpy数组
    dfdata = np.reshape(dfdata, (len(col), len(idx)))

    # dataframe实例初始化
    df = DataFrame(dfdata, columns=col, index=idx)

    # pcolor传入绘图数据，cmap指定绘图颜色，比如Blues，Greens
    plt.pcolor(df, cmap = plt.cm.Greens, edgecolors = 'white')

    # xy轴的刻度和label，刻度用的是数据切片
    plt.yticks(np.arange(1, len(df.index)+1), df.index)
    plt.xticks(np.arange(1, len(df.columns)+1), df.columns)

    plt.colorbar()
    plt.show()

def fileopen(f):
    a = []
    with open(f) as f:
        a  = f.read().split()
        # print(a)
    return a

if __name__ == '__main__':
    a = fileopen('1.txt')
    # plot heat map
    plotfuc(a, a, '3.txt')
