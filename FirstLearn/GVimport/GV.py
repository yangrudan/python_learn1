# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/16 15:26
@Author:      CookieYang
@FileName:    GV.py
@SoftWare:    PyCharm
@brief:       看看import模块的实现方式
"""

global g_intValNew


def init():
    global g_intValNew
    g_intValNew = 0


def setVal(val: int):
    global g_intValNew
    g_intValNew = val


def getVal() -> int:
    global g_intValNew
    return g_intValNew


# global g_intVal
# g_intVal = 1

print("====================This is GV fire========================")
