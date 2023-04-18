# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/18 14:42
@Author:      CookieYang
@FileName:    threadVsProcess.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import time
from threading import Thread
from multiprocessing import Process


def f1():
    time.sleep(1)  #io密集型
    # 计算型:
    # n = 10
    # for i in range(10000000):
    #     n = n + i

if __name__ == '__main__':
    # 查看一下100个线程执行100个任务的执行时间
    t_s_time = time.time()
    t_list = []
    for i in range(100):
        t = Thread(target=f1,)
        t.start()
        t_list.append(t)
    [tt.join() for tt in t_list]
    t_e_time = time.time()
    t_dif_time = t_e_time - t_s_time
    print('===================================')
    # 查看一下100个进程执行同样的任务的执行时间
    p_s_time = time.time()
    p_list = []
    for i in range(100):
        p = Process(target=f1,)
        p.start()
        p_list.append(p)
    [pp.join() for pp in p_list]
    p_e_time = time.time()
    p_dif_time = p_e_time - p_s_time
    print('多线程的执行时间:',t_dif_time)
    print('多进程的执行时间:',p_dif_time)