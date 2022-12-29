# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/16 15:35
@Author:      CookieYang
@FileName:    GV_import2.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
'''
from GV import g_intVal

def GetGvVal2():
    global g_intVal
    print("file-import2", g_intVal)
    # print("file-import2", globals()['g_intVal'])
# globals()['g_intVal'] = globals()['g_intVal']+100
# print("file-1", globals()['g_intVal'])

'''

import GV

def GetGvVal2():
    val = GV.getVal()
    print("get file 2", val)
