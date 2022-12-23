# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/23 16:48
@Author:      CookieYang
@FileName:    mainGV.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

from GV_import1 import SetGvVal
from GV_import2 import GetGvVal2
from GV_import3 import GetGvVal3
import threading
import time

if __name__ == '__main__':
    t1 = threading.Thread(target=SetGvVal, args=())
    t1.start()
    time.sleep(3)
    t2 = threading.Thread(target=GetGvVal2, args=())
    t2.start()
    time.sleep(3)
    t3 = threading.Thread(target=GetGvVal3, args=())
    t3.start()
    print("end", '='*40)
