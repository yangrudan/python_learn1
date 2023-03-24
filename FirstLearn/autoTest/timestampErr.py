# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/16 15:46
@Author:      CookieYang
@FileName:    timestampErr.py
@SoftWare:    PyCharm
@brief:       订阅时间戳异常判断
"""

import enum


ERR = enum.Enum(1, 2, 3)
'''
1. 起始时间over；
2. 结束时间over;
'''
def overTime(tDesiredStart, tDesiredEnd, tActual):
    if tActual > tDesiredStart:
        return -1
    elif tActual > tDesiredStart:
        return -2
    else:
        return 0  #正常范围内的时间流逝