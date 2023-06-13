# -*- coding: utf-8 -*-
""" 
@Time:        2023/6/12 16:20
@Author:      CookieYang
@FileName:    near.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
# 编写程序自动生成0到100间的一个随机数，然后让参与者输入昵称和数字，最后判断谁猜得最准。
import random
import numpy as np

y = random.randrange(1, 100)
res = {}
n = int(input('请输入游戏总人数:\n'))
a = 0
print('谜底是:', y)
while (a < n):
    name = input('请输入姓名:\n')
    ans = int(input('请输入数字:\n'))
    res[name] = ans
    a = a + 1
grades = list(res.values())  # 记录了每个参赛者的答案
# 不足  best_grade = min(grades, key=lambda x: abs(x - y))

grades_abs = list(map(lambda x: abs(x - y), grades))  # 记录了每个参赛者和谜底的接近程度
peo_grade = list(np.where(np.array(grades_abs) == min(grades_abs))[0])  # 记录了最接近谜底的参赛者

peo_in = [grades[i] for i in peo_grade]

best_players = ','.join([k for k, v in res.items() if v in peo_in])
print('猜的最准的是:', best_players)