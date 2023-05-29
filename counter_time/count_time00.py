# -*- coding: utf-8 -*-
""" 
@Time:        2023/5/29 14:34
@Author:      CookieYang
@FileName:    count_time00.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import time


#  装饰器run_time,@run_time加在谁头上，谁就是参数fun
def run_time(fun):
    start_time = time.time()
    fun()
    end_time = time.time()

    print("程序运行时间为：{} 秒".format(str(round((end_time - start_time), 1))))
    return end_time - start_time


#  耗时任务task
@run_time
def task():
    time.sleep(3)


if __name__ == '__main__':
    task()