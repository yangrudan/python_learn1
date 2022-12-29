# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/23 17:29
@Author:      CookieYang
@FileName:    yeildL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
def h():
    print("yang")
    yield 5
    yield 6
    print("RD")

c = h()
print(c)