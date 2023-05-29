# -*- coding: utf-8 -*-
""" 
@Time:        2023/5/29 14:48
@Author:      CookieYang
@FileName:    time_per.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import time

if __name__ == '__main__':
    start_time = time.perf_counter()
    time.sleep(6)
    # end = time.perf_counter()
    # time_now = time.perf_counter()
    # lambda x: "Even" if x % 2 == 0 else "Odd"
    # if lambda x: x - start_time > 5 (time_now):
    time_long = lambda x: True if x - start_time > 5 else False
    if time_long(time.perf_counter()):
        print("over time")
    else:
        print("less time")
