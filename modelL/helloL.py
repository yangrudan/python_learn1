# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/7 9:31
@Author:      CookieYang
@FileName:    helloL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""


def process(dict1):
    dict2 = {}
    dict2.update(dict1)
    dict1["name"] = "cookie"
    del dict2["age"]
    print(dict2['name'])
    print("end")
    print(dict1)


if __name__ == '__main__':
    my_dict = {"name": "yang",
             "age": 27}
    process(my_dict)
    print('=========================')
    print(my_dict)