# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/14 22:13
@Author:      CookieYang
@FileName:    array1.py
@SoftWare:    PyCharm
"""

import numpy as np

a = np.array((1, 2, 3, 4))
b = np.array([1, 2, 3, 4, 5])
print(a)
print(b)
c = np.split(b, [3])
print(f"c is:{c}")

a = np.zeros((3, 3))
b = np.empty((3, 4))
c = np.ones((3, 3))
d = np.full((3, 4), 5.0)
print(a)
print()
print(b)
print()
print(c)
print()
print(d)
a = np.linspace(1,10,10)
print(f"a is {a}")
b = np.arange(0,10,2)

a = np.random.rand(3, 3)
print(a)
b = a.astype('int')
print(b)

a = np.arange(9).reshape(3, 3)
b = np.arange(9, 18).reshape(3, 3)
c = np.hstack((a, b))
print(f"a is {a}")
print(f"b is {b}")
print(f"c is {c}")

listA = [1, 3, 5, 7, 9]
listB = [1,1,1,2,3,4,"str"]
a = 'aaaaa'
print(f'listB is{listB}')
print(type(a))
print(type(listB))