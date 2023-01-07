# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/6 16:06
@Author:      CookieYang
@FileName:    changeLongName2Short.py
@SoftWare:    PyCharm
@brief:       遍历文件夹里如spe_2.400000000000000000003.sim的文件，重命名为spe_2.4.sim

"""
import os


def getAllFiles(path) -> list:
    """
    @brief: 获取路径下所有文件名字
    :param path: 路径
    :return: 名字列表
    """
    res = os.listdir(path)
    print(res)
    return res


def changeFileNameShort(nameList, path):
    """
    将很长的文件名变短，目前按照一位小数设计2.4， 3.6
    以下划线作为开头；
    以后缀.作为结尾。
    :param nameList: 所有文件名称
    :param path: 文件路径
    :return: None
    """
    for name in nameList:
        oldNum = name[name.find('_') + 1: name.find("\\.")]
        print(oldNum)
        if len(oldNum) > 5:
            newName = oldNum[0:3]
            newName += ".si"
            print("---", newName)
            nameNew = name.replace(oldNum, newName)
            print("++++", name, "---", nameNew)
            try:
                os.rename(path + "/" + name, path + "/" + newName + "m")
            except Exception as e:
                print(e)


if __name__ == '__main__':
    path = "C:/Users/Administrator/Desktop/sim"
    nameList = getAllFiles(path)
    changeFileNameShort(nameList, path)
