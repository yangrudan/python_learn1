# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/13 13:34
@Author:      CookieYang
@FileName:    classSave.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import pickle
import numpy as np


class PreSaveData:
    def __init__(self, name, data):
        self.name = name
        self.data = data


def saveDump(cls):
    fBin = open("save.bin", 'ab')
    pickle.dump(cls, fBin)
    fBin.close()


def readLoad():
    f = open("save.bin", 'rb')
    while True:
        try:
            saveCls = pickle.load(f)
            print(saveCls.name)
            print(saveCls.data)
            print("==" * 40)
        except Exception as err:
            print(err)
            break
    f.close()


if __name__ == '__main__':
    """"""
    # 创建待自定义类对象
    myCls = PreSaveData("数据一号", np.linspace(0, 8000 * 200 - 1, 8000*200))
    myCls2 = PreSaveData("数据二号", np.linspace(0, 8000 * 181 - 1, 8000*181))

    # 保存文件
    saveDump(myCls)
    saveDump(myCls2)

    # 读取文件
    readLoad()

    # 结束
    print("==END==")
