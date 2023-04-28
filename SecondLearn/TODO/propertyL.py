# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/10 16:06
@Author:      CookieYang
@FileName:    propertyL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""


def getx(self):
    print("1")
    return self._x


def setx(self, value):
    print("2")
    self._x = value


def delx(self):
    print("3")
    del self._x


# create a property
x = property(getx, setx, delx, "I am doc for x property")

class Val:
    _x = 0

@setx(Val, 4)
def x():
    _x = 3
