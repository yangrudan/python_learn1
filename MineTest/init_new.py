# -*- coding: utf-8 -*-
""" 
@Time:        2023/3/3 15:30
@Author:      CookieYang
@FileName:    init_new.py
@SoftWare:    PyCharm
@brief:       init时出错
"""

g_dict = {
    "Math": 13,
    "English": 14
}


class Subscriber:
    # def __new__(cls, name):
    #     return cls

    def __init__(self, name2):
        self.age = 27
        if name2 not in g_dict:
            print("not exist")
            return None


my_subscribe = Subscriber("Math")
print(my_subscribe.age)
my_subscribe2 = Subscriber("Mathhhh")
print(my_subscribe2.age)
