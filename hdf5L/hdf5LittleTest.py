# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/27 14:34
@Author:      CookieYang
@FileName:    hdf5LittleTest.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

import h5py  #导入第三方库
import numpy as np

Data = np.linspace(0, 512*16000-1, 512*16000) #  *2*3600*24)

with h5py.File("file111.h5", 'w') as h5_f:
    dataset1 = h5_f.create_dataset("raw_data", (0, 512*16000,), maxshape=(None, None,), dtype="float")
    dataset2 = h5_f.create_dataset("timestamp", (0,), maxshape=(None,), dtype=int)

    for i in range(1500):  # 循环1500次差不多100个GB
        dataset1.resize((dataset1.shape[0] + 1, dataset1.shape[1],))
        dataset1[dataset1.shape[0]-1] = Data
        dataset2.resize((dataset2.shape[0] + 1,))
        dataset2[dataset2.shape[0] - 1] = i

