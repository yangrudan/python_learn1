# -*- coding: utf-8 -*-
""" 
@Time:        2023/2/16 14:44
@Author:      CookieYang
@FileName:    jsonUse.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

import json
import pickle

"""两种方式都可以"""
"""
补充nametuple\simplenamespace\dict\jsonDecoder方式
"""



"""() 括号看起来没有什么区别，难道是C++生成库的时候不一样？？"""
class student:
    def __init__(self):
        self.name = "YANG"


Mydict = {
    "stu": student,

    "hhh": 1
}

if __name__ == '__main__':
    me = Mydict["stu"]()
    print(me.name)