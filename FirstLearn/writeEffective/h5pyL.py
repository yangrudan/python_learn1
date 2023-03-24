# -*- coding: utf-8 -*-
""" 
@Time:        2023/2/3 14:05
@Author:      CookieYang
@FileName:    h5pyL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

import h5py
import numpy as np


f = h5py.File("111.h5", 'w')
data = np.linspace(0, 9999, 10000)
dset1 = f.create_dataset("1", data=data)
dset1.attrs['info'] = "a"

dset2 = f.create_dataset("2", data=data)
dset2.attrs['info'] = "b"

f.close()

f = h5py.File('111.h5', 'r')  # 打开h5文件
print(f.keys())
a = f['1'][:]  # 取出主键为1的所有的键值
print(a)
b = f['2'][:]  # 取出主键为1的所有的键值
print(b)
f.close()
