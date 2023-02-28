# -*- coding: utf-8 -*-
""" 
@Time:        2023/2/28 14:03
@Author:      CookieYang
@FileName:    numpyL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""


import numpy as np

data = np.ones((2, 3, 6))                             # 从外到内
print(data)

data2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])   # (3, 3)
print(data2.shape)

data3 = np.arange(1, 28, 1)
data4 = data3.reshape(3, 3, 3)
print(data4)
print(data4.max(axis=2))                              # 低维比向量，高维比元素


