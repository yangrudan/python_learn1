# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/18 14:31
@Author:      CookieYang
@FileName:    multiprocess00L.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

# coding: utf-8
import multiprocessing
import time


def func():
    msg = "ok"
    print("msg:", msg)
    time.sleep(0.01)
    print("end")


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=3)
    for i in range(20):
        msg = "hello %d" % (i)
        pool.apply_async(func)  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print("wait close~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("done")