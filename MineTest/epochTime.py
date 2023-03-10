# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/12 13:38
@Author:      CookieYang
@FileName:    epochTime.py
@SoftWare:    PyCharm
@brief:       epoch时间转换
"""

import time

import numpy as np
import datetime

'''
#打印epoch  Time
print(time.time())
#打印GMT时间
print(time.gmtime())
#打印本地时间
print(time.localtime())
'''

print(time.gmtime(0))
'''epoch时间转换成local time'''
epoch_time = 946730040.333444555
strTime = time.strftime("时间：%Y年%m月%d日 %H时%M分%S秒", time.localtime(epoch_time))#"%a, %d %b %Y %H:%M:%S"
print(strTime)


dt = datetime.datetime.fromtimestamp(epoch_time)
print(dt)

timeLocal = time.localtime(epoch_time)
print(timeLocal)


'''格式化时间转换成epoch time'''
print('===================================================')
time1 = time.strptime(strTime, "时间：%Y年%m月%d日 %H时%M分%S秒")
print(time1)
time2 = time.mktime(time1)
print(time2)


a = np.array([time.time() * 10**9])  # epoch seconds to ns
print(a)
np.array([1.60473147e+18])
a = np.asarray(a, dtype='datetime64[ns]')
print(a)
np.array(['2020-11-07T06:44:29.714103040'], dtype='datetime64[ns]')
print("=================")