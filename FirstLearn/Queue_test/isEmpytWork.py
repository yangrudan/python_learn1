# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/6 11:22
@Author:      CookieYang
@FileName:    isEmpytWork.py
@SoftWare:    PyCharm
@brief:       判断队列的notEmpty是否可以判断成功
"""
import queue

if __name__ == '__main__':
    data = queue.Queue()
    data.put(1)
    # print(type(data.not_empty))
    print(data.empty())
    try:
        print(data.get(block=False))
    except queue.Empty:
        print("空")
        print("END")