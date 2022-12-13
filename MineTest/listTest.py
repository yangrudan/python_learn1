# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/5 15:49
@Author:      CookieYang
@FileName:    listTest.py
@SoftWare:    PyCharm
@brief:       验证list参数传递的是不是指针，传递名字改变内部值，是的
"""

def changeList(list:list):
    list.append("1")

if __name__ == '__main__':
    subscribes = []
    changeList(subscribes)
    print(subscribes)
    changeList(subscribes)
    print(subscribes)