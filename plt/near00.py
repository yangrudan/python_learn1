# -*- coding: utf-8 -*-
""" 
@Time:        2023/6/12 16:20
@Author:      CookieYang
@FileName:    near00.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import numpy as np

grades = np.array(range(100))
y = 80.5


grades_abs = list(map(lambda x: abs(x - y), grades))
peo_grade = list(np.where(np.array(grades_abs) == min(grades_abs))[0])
print(peo_grade)