# -*- coding: utf-8 -*-
""" 
@Time:        2023/5/25 10:03
@Author:      CookieYang
@FileName:    del_new_cls.py
@SoftWare:    PyCharm
@brief:       功能简介
"""


class MyClass:
    def __new__(cls):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ called")
        self.name = "MyClass"

    def __del__(self):
        print("__del__ called")


obj = MyClass()
print(obj.name)
# del obj


# class Dog():
#     def __del__(self):
#         print("---对象要发财了--")
# dog1 = Dog() #对象dog1 与对象dog2指向同一个对象
# dog2 = dog1
# del dog1
# del dog2    #当把这句话注释起来先打印下面那句也就是“=====”，因为程序结束，对
# # 象被销毁，在释放内存时自动调用__del__方法。当这句话没被注释，dog1,dog2都被删除了相当
# # 于对象被删除了（当只删除dog1或dog2，对象还存在），在释放内存时会调用__del__方
# # 法，所以"---对象要死掉了--"先被 打印了出来
# print("=====")
#
# # __del__ 方法， 当对象“死”的时候，也就意味着对象的内存空间要被释放，当它释放，
# # 当对象马上要死的时候，__del__方法会被自动调用