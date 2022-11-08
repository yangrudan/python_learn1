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

if __name__ == '__main__':
    #建立一个空字典
    dic = {}
    for i in range(500, 1000, 100): #设定开始,结束，步长.
        dic[str(i)] = doubleNum(i)
    print(f"dic[500] = {dic[str(500)]}")
    print(f"dic[600] = {dic[str(600)]}")
    print(f"dic[700] = {dic[str(700)]}")
    print(f"dic[800] = {dic[str(800)]}")
    print(f"dic[900] = {dic[str(900)]}")

