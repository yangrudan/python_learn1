# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/9 11:21
@Author:      CookieYang
@FileName:    saveAbsolutePath.py
@SoftWare:    PyCharm
@brief:       绝对路径存储
"""


import os

if __name__ == '__main__':
    path = "name.txt"
    res = os.path.join("", path)
    print(res)
    open(res, 'w')














