# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/23 17:29
@Author:      CookieYang
@FileName:    yeildL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
# def h():
#     print("yang")
#     # yield 5
#     # yield 6
#     print("RD")
#
# c = h()
# print(c)


# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print("______________")
# print(next(g))
# print("*"*20)
# print(next(g))
# print("*"*20)
# print(next(g))



def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(0):
    print(n)