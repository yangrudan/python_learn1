# -*- coding: utf-8 -*-
""" 
@Time:        2023/2/16 14:35
@Author:      CookieYang
@FileName:    apiCall.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import requests
import os, re
import urllib.request

data = {"email": "251910179@qq.com", "password": "ydd4903087"}
session = requests.session()
session.post("http://www.renren.com/PLogin.do", data=data, verify=False)
response = session.get("http://www.renren.com/410043129/profile")
print(response.text)
print(response.url)
print(response.status_code)
print(response.headers)

# 爬网页图片：

requset = requests.post("http://tieba.baidu.com/p/4114581614", verify=False)

r = r'src="(http://imgsrc.baidu.com/.*?\.jpg)"'
# r=r'http://imgsrc.baidu.com/.+?\.jpg'
mylist = re.findall(r, str(requset.text))
print(mylist)
j = 0
for i in mylist:
    urllib.request.urlretrieve(i, "C:/Users/Administrator/Desktop/img1/" + str(j) + ".jpg")
    j += 1