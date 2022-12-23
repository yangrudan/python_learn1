# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/16 15:35
@Author:      CookieYang
@FileName:    GV_import1.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

from GV import g_intVal

def SetGvVal():
    globals()['g_intVal'] = 100
    print("file-1", globals()['g_intVal'])
