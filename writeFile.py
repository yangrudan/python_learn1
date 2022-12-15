# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/13 15:48
@Author:      CookieYang
@FileName:    writeFile.py
@SoftWare:    PyCharm
@brief:       从numpy数组保存为文件
"""

'''
w         |以写方式打开
a         |以追加方式打开（从EOF开始，必要时创建新文件）
r+        |以读写方式打开
w+        |以读写方式打开
a+        |以读写方式打开
rb        |以二进制读方式打开
wb        |以二进制写方式打开
ab        |以二进制追加方式打开
rb+       |以二进制读写方式打开
wb+       |以二进制读写方式打开
ab+       |以二进制读写方式打开
'''

import os
import numpy as np


a = np.linspace(0, 512*16000-1, 512*16000)
print(a)
b = np.array(a)
print(b)
c = b.tolist()
print(c)

# with open("nparray.txt", "ab") as f:
#     f.write(c)

# f = open("nparray1.txt", 'w')
# f.write("hello")
# f.close()

np.savetxt("nparray1.txt", c)
print(os.path.abspath(__file__))