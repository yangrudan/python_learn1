# -*- coding: utf-8 -*-
""" 
@Time:        2023/6/15 16:34
@Author:      CookieYang
@FileName:    lineL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from sklearn.linear_model import LinearRegression
import numpy as np


apple = np.array([155,156,157])
n = len(apple)
model = LinearRegression().fit(np.arange(n).reshape((n,1)), apple)
print(model.predict([[3], [4]]))
