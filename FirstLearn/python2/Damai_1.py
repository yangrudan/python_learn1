# -*- coding: utf-8 -*-
""" 
@Time:        2023/3/24 13:19
@Author:      CookieYang
@FileName:    Damai_1.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# url地址
url = 'http://www.baidu.com'

# 定义chrome驱动去地址
path = Service('chromedriver.exe')
print(path)

# 创建浏览器操作对象
browser = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', service=path)
browser.get(url)
print("+++")