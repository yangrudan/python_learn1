# -*- coding: utf-8 -*-
""" 
@Time:        2023/3/7 17:34
@Author:      CookieYang
@FileName:    callbackAscyn.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

def apply_ascyn(func, args, callback):
    """
    func 函数的是处理的函数
    args 表示的参数
    callback 表示的函数处理完成后的 该执行的动作
    """
    result = func(*args)
    callback(result)

def add(x, y):
    return x + y

def print_result(result):
    print(result)


apply_ascyn(add, (2, 3), callback=print_result)  # 5


def my_callback(args):
    print(*args)


def caller(args, func):
    func(args)


caller((1, 3), my_callback)


def appy_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def add(x ,y):
    return x + y

class ResultHandler(object):
    def __init__(self):
        self.sequence = 0

    def handle(self, result):
        self.sequence += 1
        print("[{}] Got: {}".format(self.sequence, result))


r = ResultHandler()
appy_async(add, (2,3), callback=r.handle)
appy_async(add, (2,3), callback=r.handle)