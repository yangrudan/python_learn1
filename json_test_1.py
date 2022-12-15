# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/27 19:59
@Author:      CookieYang
@FileName:    json_test_1.py
@SoftWare:    PyCharm
"""
from enum import Enum
from typing import Union
import json
from json import JSONEncoder

'''
@brief:
以下xxInfo表示TCP传递的信息结构体内的info
'''
class SubscribeInfo(object):
    def __init__(self,paraName, *args, **kwargs):
        self.head = 0xabcd
        self.paraName = paraName
        self.timeStart = ""
        self.timeEnd = ""
        self.tail = 0xdcba


class DataTransEncoder(JSONEncoder):
    def default(self, o):
        print(o.__dict__)
        print('333333333333')
        return o.__dict__


info = SubscribeInfo(paraName = "aaa")

# encode Object it
dataJson = json.dumps(info, cls=DataTransEncoder)
print(f'ppppppppp{type(dataJson)}')

# Deconde JSON
resultDict = json.loads(dataJson)
print(f'22222222222{type(resultDict)}')

print("Converting JSON into Python Object")
dataObj = SubscribeInfo(**resultDict)

print("Object type is: ", type(dataObj))

print("dataObj Details")
print(dataObj.__dict__)
print(dataObj.paraName)