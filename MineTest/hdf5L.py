# -*- coding: utf-8 -*-
""" 
@Time:        2023/2/28 15:45
@Author:      CookieYang
@FileName:    hdf5L.py
@SoftWare:    PyCharm
@brief:
具有约10 ^ 4列和约10 ^ 7行。 (这大约是10 ^ 11(1000亿)个元素，或1个字节整数的?100GB)。
有了这些数据，通常的用途是一次写入，多次读取，并且典型的读取情况是抓取第1列和另一列(例如254)，将两列都加载到内存中，并进行一些统计。

现在的问题是：
我一次接收到大约10 ^ 4行的数据(并且每次接收的行数不完全相同)，并且需要将其递增地写入hdf5文件。如何写那个文件？
"""
import h5py

with h5py.File("data.hdf5", "w") as f:
    dset = f.create_dataset("voltage284", (100000,), maxshape=(None,), dtype='i8', chunks=(10000,))

import os
import h5py
import numpy as np
path = './tmp/out.h5'
os.remove(path)
with h5py.File(path,"a") as f:
    dset = f.create_dataset('voltage284', (10**5,), maxshape=(None,),
                            dtype='i8', chunks=(10**4,))
    dset[:] = np.random.random(dset.shape)
    print(dset.shape)
    # (100000,)

    for i in range(3):
        dset.resize(dset.shape[0]+10**4, axis=0)
        dset[-10**4:] = np.random.random(10**4)
        print(dset.shape)

    print("end")