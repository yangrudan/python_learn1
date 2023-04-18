# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/18 14:25
@Author:      CookieYang
@FileName:    multiprocessL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import time
from multiprocessing import Pool


def f(x):
    time.sleep(10)
    # n = 10
    # for i in range(10000000):
    #     n = n + i
    return x * x


if __name__ == '__main__':
    with Pool() as p:
        max_count = 10000
        time1 = time.time()
        res = p.map(f, range(1, max_count + 1))
        print(sum(res))
        time2 = time.time()
        print(f"{max_count}，耗时：{time2 - time1:.2f}秒")