# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/22 14:08
@Author:      CookieYang
@FileName:    线程池.py
@SoftWare:    PyCharm
@brief:       线程持初览
"""
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures


def add(num):
    """
    简单的函数，每个线程去调用，输入参数+1
    :param num:
    :return:
    """
    num += 1
    return num


with ThreadPoolExecutor(max_workers=10) as pool:
    def get_result(future):
        """
        用于注册线程池的回调函数
        :param future:
        :return:
        """
        print(future.result())


    futuresList = []
    for i in range(100):  # 添加100个线程
        futuresList.append(pool.submit(add, 100))

    '''方式一'''
    results = []
    for future in futures.as_completed(futuresList):  # 等待完成
        res = future.result()  # 接收结果
        results.append(res)
        print("Already Finished", res)
    print(results)
    '''方式二'''
    for threadWork in futuresList:
        threadWork.add_done_callback(get_result)


print("==END==")
