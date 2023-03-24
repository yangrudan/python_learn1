# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/22 9:40
@Author:      CookieYang
@FileName:    byWraps.py
@SoftWare:    PyCharm
@brief:       功能简介: 通过装饰器实现
"""

from functools import wraps


def singleton(cls):
    """单例类装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    pass

if __name__ == '__main__':
    my_president = President()
    print(my_president)

    a = 3
    b = 4
    # a, b = b,a
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)