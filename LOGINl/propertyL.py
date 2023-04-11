# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/10 16:06
@Author:      CookieYang
@FileName:    propertyL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""


def getx(self):
    return self._x


def setx(self, value):
    self._x = value


def delx(self):
    del self._x


# create a property
x = property(getx, setx, delx, "I am doc for x property")
