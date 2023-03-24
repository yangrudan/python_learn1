# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/7 18:12
@Author:      CookieYang
@FileName:    defaultDict.py
@SoftWare:    PyCharm
@brief:       即使容器为空也不报错
"""

from collections import defaultdict

dict1 = defaultdict(int)  # dict1[1]=0
dict2 = defaultdict(set)  # dict2[1]=set()
dict3 = defaultdict(str)  # dict3[1]=
dict4 = defaultdict(list)  # dict4[1]=[]

print(dict4[2])