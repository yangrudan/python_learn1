# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/11 17:06
@Author:      CookieYang
@FileName:    run.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import os
# from dotenv import load_dotenv

# load_dotenv()

key = 'MY_NAME'

value = os.getenv(key)

print("Value of 'HOME' environment variable :", value)
