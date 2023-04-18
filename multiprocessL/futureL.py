# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/18 14:24
@Author:      CookieYang
@FileName:    futureL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from concurrent.futures import ProcessPoolExecutor
import time


def f(x):
    time.sleep(0.1)
    return x * x


if __name__ == '__main__':
    with ProcessPoolExecutor() as p:
        max_count = 100
        time1 = time.time()
        res = p.map(f, range(1, max_count + 1))
        print(sum(res))
        time2 = time.time()
        print(f"{max_count}，耗时：{time2 - time1:.2f}秒")