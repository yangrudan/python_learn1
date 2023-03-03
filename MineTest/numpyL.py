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
""" [data]
[[[1. 1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1. 1.]]]
"""

data2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])   # (3, 3)
print(data2.shape)  # (3, 3)

data3 = np.arange(1, 28, 1)
data4 = data3.reshape(3, 3, 3)
print(data4)
""" [data4]
[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]
  [25 26 27]]]
"""
print(data4.max(axis=2))                              # 低维比向量，高维比元素
"""
[[ 3  6  9]
 [12 15 18]
 [21 24 27]]
"""

