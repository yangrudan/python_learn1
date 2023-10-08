# -*- coding: utf-8 -*-
""" 
@Time:        2023/5/25 10:45
@Author:      CookieYang
@FileName:    Cctrl.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import signal
import time


def SigIntHand(SIG, FRM):
    print("Please Right click-copy. Ctrl-C does not work on the cmd prompt")

signal.signal(signal.SIGINT, SigIntHand)
while 1:
    print("222")
    time.sleep(2)