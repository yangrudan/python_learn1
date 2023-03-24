# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/11 15:51
@Author:      CookieYang
@FileName:    csvSave.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import pandas as pd
list=[[1,2,3],[4,5,6],[7,8,9]]
name=["id","uid","time"]
test=pd.DataFrame(columns=name, data=list)
test.to_csv("test.csv")