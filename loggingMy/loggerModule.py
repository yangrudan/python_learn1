# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/14 16:42
@Author:      CookieYang
@FileName:    loggerModule.py
@SoftWare:    PyCharm
@brief:       封装成类
"""
import logging
from logging import handlers


class Logger(object):
    def __init__(self, log_name, level):
        self.logger = logging.getLogger(log_name)  # 获取记录器，并设置记录器的名字
        # 设置格式
        format = logging.Formatter(
            """%(asctime)s  - %(levelname)s: %(message)s - %(pathname)s[line:%(lineno)d]""")
        # 设置显示级别
        self.logger.setLevel(level)
        # 实例将消息发送到硬盘文件，以特定的时间间隔轮换日志文件，具体看官方文档
        tfh = handlers.TimedRotatingFileHandler(filename=log_name, when="D", backupCount=0, encoding="utf-8")
        tfh.setFormatter(format)
        self.logger.addHandler(tfh)

    def writeInfo(self):
        self.logger.info("运行信息是：{0}".format("hello"))


global myLogger
myLogger = Logger("log.log", logging.DEBUG)

