# -*- coding: utf-8 -*-
"""
@Author:      CookieYang
@FileName:    readH5.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import h5py
import numpy as np


f = h5py.File("file111.h5", "r")
print([key for key in f.keys()], "\n")

print(type(f['timestamp']))
ls = list(f['timestamp'])
index = ls.index(500)  # 通过Value，反向找到index
print("==index==", index)

print(type(f['raw_data']))
print(f['raw_data'][index, 0:4])
res = np.sum(f['raw_data'][index, :])
f.close()