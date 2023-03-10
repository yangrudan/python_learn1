# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/27 21:00
@Author:      CookieYang
@FileName:    class2Json.py
@SoftWare:    PyCharm----
"""

import json
from json import JSONEncoder
import logging

logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s -%(message)s")

class SubscribeInfo(object):
    def __init__(self,paraName, timeStart = "20221127", timeEnd = "20221128", errInfo = "", *args, **kwargs):
        self.head = 0xabcd
        self.paraName = paraName
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.errInfo = errInfo
        self.tail = 0xdcba


class DataTransEncoder(JSONEncoder):
    def default(self, o):
        logging.debug(str(o.__dict__))
        return o.__dict__

def wrapCls(clsInstance):
    return json.dumps(clsInstance, cls=DataTransEncoder)

def str2Cls(dataJson):
    # Deconde JSON
    resultDict = json.loads(dataJson)
    dataObj = SubscribeInfo(**resultDict)
    logging.debug(dataObj.paraName)
    return dataObj


def judgeStrIsSubscribeCls(strData):
    try:
        clsObj = str2Cls(strData)
    except Exception as err:
        clsObj = None
    return clsObj

'''
@brief:
    Test
'''
'''
info = SubscribeInfo(paraName = "aaa", timeStart= 20223)
strData = wrapCls(info)
str2 = "yyyyy"
res = judgeStrIsSubscribeCls(str2)
print(res)
obj = str2Cls(strData)
print(obj.tail)
print(obj.timeStart)
'''
