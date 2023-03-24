# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/22 10:42
@Author:      CookieYang
@FileName:    byWrap2.py
@SoftWare:    PyCharm
@brief:       功能简介 init函数里传递了参数
"""


def singleton(cls):
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


@singleton
class Demo3(object):

    def __init__(self, x=0):
        self.x = x


a1 = Demo3(5)
a2 = Demo3(2)
print(id(a1))
print(id(a2))
print(a2.x)
print(a1.x)
