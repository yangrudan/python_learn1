# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/14 15:55
@Author:      CookieYang
@FileName:    globalLogMain.py
@SoftWare:    PyCharm
@brief:       公用一个打印级别控制器
"""
import logConsole

if __name__ == '__main__':
    logConsole.init()
    logConsole.logLevelController.critical("是不是全局可控就看你了")
