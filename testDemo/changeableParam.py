# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/15 10:25
@Author:      CookieYang
@FileName:    changeableParam.py
@SoftWare:    PyCharm
@brief:       可变参数个数的函数
"""
#可变形参之*——存储元组的方式
def func(*args):
    print("len", len(args))
    print(args)

#可变形参之**——存储字典的方式
def func1(**kwargs):
    print(len(kwargs))
    print(kwargs)

if __name__ == '__main__':
    func()
    func(1)
    func(1,2)
    func1(b=5, c=6)