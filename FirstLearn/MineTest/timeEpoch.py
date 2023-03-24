# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/7 17:56
@Author:      CookieYang
@FileName:    timeEpoch.py
@SoftWare:    PyCharm
@brief:       UTC世界协调时、epoch time、时间戳
"""

import time
import datetime

if __name__ == '__main__':
    print(time.localtime())  # Fri Mar 10 11:46:52 2023

    epoch_time = 1622235931.000500000  # epoch time 2 str
    strTime = time.strftime("时间：%Y年%m月%d日 %H时%M分%S秒", time.localtime(epoch_time))
    print(strTime)  # 时间：2021年05月29日 05时05分31秒

    dt = datetime.datetime.fromtimestamp(epoch_time)
    print("dt", dt)  # dt 2021-05-29 05:05:31.000500


