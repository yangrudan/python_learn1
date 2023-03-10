# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/22 10:52
@Author:      CookieYang
@FileName:    byClass2.py
@SoftWare:    PyCharm
@brief:       功能简介  怎么应用呢？
"""

class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 判断类属性是否是空对象
        if cls.instance is None:

            # 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象引用
        return cls.instance

# 创建多个对象
play1 = MusicPlayer()
print(play1)

play2 = MusicPlayer()
print(play2)
