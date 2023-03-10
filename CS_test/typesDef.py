# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/25 19:10
@Author:      CookieYang
@FileName:    typesDef.py
@SoftWare:    PyCharm
@brief:       接口类型定义V1.0
"""
#TODO;;;;;;;转换JSON报错__init__() missing 1 required positional argument:
from enum import Enum
from typing import Union

'''
@brief:
以下xxInfo表示TCP传递的信息结构体内的info
'''
class SubscribeInfo:
    def __int__(self):
        self.paraName = ""
        self.timeStart = ""
        self.timeEnd = ""

class UnsubscribeInfo:
    def __int__(self):
        self.paraName = ""

'''
@brief:
transInfo表示TCP传递的信息结构体的具体信息
'''
transInfo = Union[SubscribeInfo, UnsubscribeInfo]

'''
@brief:
transCmdType表示TCP传递的信息结构体内的cmdType
'''
transCmdType = Enum('transCmdType', \
              ('Subscribe', 'Unsubscribe'))#python的枚举值从1开始

'''
@brief:
DataTrans表示TCP传递的信息结构体
'''
class DataTrans:
    def __init__(self, cmd: transCmdType, info: transInfo):
        self.head = 0xaabbccdd
        self.cmdType = cmd
        self.info = info

'''
@brief:
判断是否是DataTrans数据
'''
def judgeIsDataTypeTransData(data):
    transData =