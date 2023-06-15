# -*- coding: utf-8 -*-
""" 
@Time:        2023/6/15 16:17
@Author:      CookieYang
@FileName:    zip00.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
zipped = zip(lst_1, lst_2)
print('==end==')

column_names = ['name', 'salary', 'job']
db_rows = [
    ('Alice', 180000, 'data_scientist'),
    ('Bob', 99000, 'mid_level_manager'),
    ('Alice', 87000, 'CEO')
]
db = [dict(zip(column_names, row)) for row in db_rows]
print(db)