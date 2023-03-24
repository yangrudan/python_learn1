# -*- coding: utf-8 -*-
""" 
@Time:        2023/3/7 17:07
@Author:      CookieYang
@FileName:    callBackL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""


# 定义类
class Demo():

    def foo(self, num):
        return self.callback_func(num)

    # 定义修饰器
    def callback(self, func):
        self.callback_func = func


# 初始化类
demo = Demo()


# 注册回调函数1
@demo.callback
def double(x):
    return 2 * x


# 调用回调函数1
print(demo.foo(3))


# 注册回调函数2
@demo.callback
def inserve(x):
    return -x


# 调用回调函数2
print(demo.foo(3))