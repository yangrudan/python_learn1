# -*- coding: utf-8 -*-
"""
@Time:        2023/6/12 11:01
@Author:      CookieYang
@FileName:    draw00.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
#导入库
import matplotlib.pyplot as plt
import numpy as np
from scipy import io
#设定画布。dpi越大图越清晰，绘图时间越久
fig=plt.figure

data_src = io.loadmat("TimeDomainAnalysis.mat")
tIdx = data_src['tIdx']
array = data_src['dataPlot']

print(tIdx)

print(array)
#导入数据
x=list(tIdx[0])
for i in array:
    y = list(i)
    plt.plot(x, y, lw=4, ls='-', c='b', alpha=0.1)

plt.plot()
plt.show()
#保存图片
fig.savefig("画布")