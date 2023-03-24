# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/14 11:16
@Author:      CookieYang
@FileName:    test_list.py
@SoftWare:    PyCharm
"""

records = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = []
for y in range(0, 4):
    for x in range(0, 3):
        if x == 0:
            result.append([])
        result[y].append(records[x + y * 3])
print(result)

list_A = [1,2,3]
list_B = [1,3,3]
if list_A == list_B:
    print("yes")
else:
    print("No")