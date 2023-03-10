# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/14 15:43
@Author:      CookieYang
@FileName:    logConsole.py
@SoftWare:    PyCharm
@brief:       输出到控制台、文件
"""

import logging

global logLevelController

def init():
    format = logging.Formatter(
        # 时间 - 日志器名 - 日志级别 - 文件路径 - 行号： 信息
        '%(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(lineno)s： %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    sh = logging.StreamHandler()  # 控制台日志记录器
    sh.setFormatter(format)  # 对象的形式设置日志格式

    globals()['logLevelController'] = logging.getLogger("MyLog")  # 设置全局日志工具对象
    globals()['logLevelController'].setLevel(logging.WARNING)  # 设置日志级别
    globals()['logLevelController'].addHandler(sh)  # 添加日志记录器到全局工具对象

    # globals()['logLevelController'].debug("写不出来  应该是滴")
    # globals()['logLevelController'].info("这是普通级别的日志信息")
    # globals()['logLevelController'].warning("这是警告级别的日志信息")
    # globals()['logLevelController'].critical("这是极重要级别的日志信息")

    # try:
    #     a = 2 / 0
    # except ZeroDivisionError as e:
    #     globals()['logLevelController'].error("错误信息：" + str(e))
    '''
    #filemode中a为追加，w为覆盖，
    #默认是Warning级别
    注释部分写入./testLog.log文件
    loggingMy.basicConfig(level=loggingMy.DEBUG, format="%(asctime)s  -%(levelname)s -%(message)s", filename='./testLog.log', filemode='a')
    '''

    # loggingMy.debug('这是一个debug级别的日志信息')
    # loggingMy.info('这是一个info级别的日志信息')
    # loggingMy.warning('这是一个warning级别的日志信息')
    # loggingMy.error('这是一个error级别的日志信息')
    # loggingMy.critical('这是一个critical级别的日志信息')


