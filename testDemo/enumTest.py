# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/24 10:38
@Author:      CookieYang
@FileName:    enumTest.py
@SoftWare:    PyCharm
"""

from enum import Enum


class Color(Enum):
    RED = '#F44336'
    BLUE = '#2196F3'
    GREEN = '#4CAF50'


print(Color.RED.value)
print(Color.BLUE)
print(Color.GREEN)

