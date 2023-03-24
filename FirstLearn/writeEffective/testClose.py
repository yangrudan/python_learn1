# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/16 9:22
@Author:      CookieYang
@FileName:    testClose.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import pickle
import threading
import time
import pandas as pd


def save():
    list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    name = ["id", "uid", "time"]
    test = pd.DataFrame(columns=name, data=list)
    test.to_csv("test0116.csv")

    list2 = [1,2,3,4]
    fBin = open("save.bin", 'ab')
    pickle.dump(list2, fBin)
    fBin.close()
    print("file ok")
    while True:
        {
            time.sleep(1)
        }



if __name__ == '__main__':
    t1 = threading.Thread(target=save, args=())
    t1.start()

    t1.join()
    print("===end===")