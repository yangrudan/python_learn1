# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/10 11:26
@Author:      CookieYang
@FileName:    decorate01_two.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
# 为函数添加一个统计运行时长的功能以及日志记录功能
import time
import threading


def how_much_time(func):
    print("how_much_time函数开始了")

    def inner():
        t_start = time.time()
        func()
        t_end = time.time()
        print("一共花费了{0}秒时间".format(t_end - t_start, ))

    return inner


def mylog(func):
    print("mylog函数开始了")

    def inner_1():
        print("start")
        func()
        print("end")

    return inner_1


@mylog
@how_much_time
# 等价于mylog(how_much_time(sleep_5s))
def sleep_5s():
    time.sleep(5)
    print("%d秒结束了" % (5,))


if __name__ == '__main__':
    sleep_5s()
# how_much_time函数开始了
# mylog函数开始了
# start
# 5秒结束了
# 一共花费了5.012601613998413秒时间
# end