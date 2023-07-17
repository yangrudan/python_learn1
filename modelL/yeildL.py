# -*- coding: utf-8 -*-
""" 
@Time:        2023/6/27 14:34
@Author:      CookieYang
@FileName:    yeildL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()
print(next(g))
print("*" * 20)
print(next(g))
