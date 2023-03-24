# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/6 14:29
@Author:      CookieYang
@FileName:    event_test.py
@SoftWare:    PyCharm
@brief:       set开启所有wait
"""
import threading
import time,random

def say(e):
    time.sleep(random.random())
    print('准备说话中。。。。')
    e.wait()
    time.sleep(random.random())
    print('%s->可以开始说话了' % (threading.current_thread().name))

e = threading.Event()
t1 = threading.Thread(target=say, args=(e,), name='线程1')
t2 = threading.Thread(target=say, args=(e,), name='线程2')
t1.start()
t2.start()

time.sleep(5)
e.set()
e.clear()