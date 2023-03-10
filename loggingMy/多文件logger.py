# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/3 16:29
@Author:      CookieYang
@FileName:    多文件logger.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from loggingMy import loggerModule
if __name__ == "__main__":
    e = "eeeeeeee"
    loggerModule.myLogger.logger.error("错误信息是：{0}".format(e))
    loggerModule.myLogger.writeInfo()

