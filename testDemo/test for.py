# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/8 11:18
@Author:      CookieYang
@FileName:    test for.py
@SoftWare:    PyCharm
"""

#输出一个数的2倍计算结果
def doubleNum(intVal):
    return (2*intVal)

#再次封装for循环输出结果，以便给其他模块使用
def forDoubleNum(startVal, stopVal, step):
    # 建立一个空字典
    dicRet = {}
    for i in range(startVal, stopVal, step): #设定开始,结束，步长.
        dicRet[str(i)] = doubleNum(i)
    return dicRet


if __name__ == '__main__':
    dic = forDoubleNum(500, 1000, 100)

    print(f"dic[500] = {dic[str(500)]}")
    print(f"dic[600] = {dic[str(600)]}")
    print(f"dic[700] = {dic[str(700)]}")
    print(f"dic[800] = {dic[str(800)]}")
    print(f"dic[900] = {dic[str(900)]}")

