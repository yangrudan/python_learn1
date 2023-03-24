# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/11 10:09
@Author:      CookieYang
@FileName:    hdf5Write.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

import h5py  # 导入工具包
import numpy as np
import time

# HDF5的写入：
imgData = np.zeros((30, 3, 128, 256))
timeStart0 = time.perf_counter()
f = h5py.File('HDF5_FILE.h5', 'w')  # 创建一个h5文件，文件指针是f
f['data'] = imgData  # 将数据写入文件的主键data下面
f['labels'] = range(100)  # 将数据写入文件的主键labels下面
f.close()  # 关闭文件
timeStart1 = time.perf_counter()
print("从创建文件到关闭文件时间： ", timeStart1-timeStart0)

# HDF5的读取：
timeStart0 = time.perf_counter()
f = h5py.File('HDF5_FILE.h5', 'r')  # 打开h5文件
f.keys()  # 可以查看所有的主键
a = f['data'][:]  # 取出主键为data的所有的键值
f.close()
timeStart1 = time.perf_counter()
print("从打开读取文件到关闭文件时间： ", timeStart1-timeStart0)
