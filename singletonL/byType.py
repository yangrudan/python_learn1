# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/22 9:35
@Author:      CookieYang
@FileName:    byType.py
@SoftWare:    PyCharm
@brief:       功能简介: 通过元类创建
"""

class SingletonMeta(type):
    """自定义单例元类"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    pass

if __name__ == '__main__':
    my_presifent = President()
    print(my_presifent)
    print(my_presifent.__class__)