# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/16 15:35
@Author:      CookieYang
@FileName:    GV_import1.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

'''
from GV import g_intVal


def SetGvVal():
    global g_intVal
    g_intVal = 100
    # globals()['g_intVal'] = 100
    print("file-1", globals()['g_intVal'])
'''

import GV


def SetGvVal():
    GV.setVal(100)
    print("set 100")
