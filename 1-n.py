# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/28 16:57
@Author:      CookieYang
@FileName:    1-n.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

n = 10
sum_val = 1
res = [sum_val + i for i in range(n)]
print(sum_val)
print(res)


def Fib(x): return 1 if x in {0, 1} else Fib(x-1) + Fib(x-2)
print(Fib(100)) # 8
