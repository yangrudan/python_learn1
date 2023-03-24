# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/7 9:16
@Author:      CookieYang
@FileName:    queueInTest.py
@SoftWare:    PyCharm
@brief:       验证有一个线程写不进去问题
"""
import queue
import threading
import time

"""管理缓冲器"""
class BuffManager:
    def __init__(self):
        self.m_buff = queue.Queue()
        self.m_lock = threading.Lock()

    def addData(self, ele):
        self.m_lock.acquire()
        self.m_buff.put(ele)
        self.m_lock.release()

    def useData(self):
        res = None
        if not self.m_buff.empty():
            self.m_lock.acquire()
            res = self.m_buff.get()
            self.m_lock.release()
        return res

g_sendBuff = BuffManager()

def thread1():
    g_sendBuff.addData(1)
    print(g_sendBuff.m_buff.qsize())

def thread2():
    g_sendBuff.addData(2)
    print(g_sendBuff.m_buff.qsize())

class getWork(threading.Thread):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):
        while True:
            ele = g_sendBuff.useData()

            if ele is None:
                time.sleep(1)
            else:
                print("ele is %d" % ele)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1, args=())
    t1.start()
    t2 = threading.Thread(target=thread2, args=())
    t2.start()
    data = None
    rcv = getWork(data)
    rcv.start()
