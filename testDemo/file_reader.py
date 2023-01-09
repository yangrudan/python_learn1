# -*- coding: utf-8 -*-
""" 
@Time:        2022/10/26 16:55
@Author:      CookieYang
@FileName:    file_reader.py
@SoftWare:    PyCharm
"""

with open("Pi_digits.txt") as file_object:
    contens = file_object.read()

print(contens.rstrip())