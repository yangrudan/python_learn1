# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/10 12:53
@Author:      CookieYang
@FileName:    decorate02-2.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import time


class Decorator:
    def __init__(self, func):
        self.func = func

    def defer_time(self, time_sec):
        time.sleep(time_sec)
        print(f"{time_sec}s延时结束了")

    def __call__(self, time):
        self.defer_time(time)
        self.func()


@Decorator
def f1():
    print("延时之后我才开始执行")


f1(5)