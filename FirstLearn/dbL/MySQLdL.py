# -*- coding: utf-8 -*-
""" 
@Time:        2023/3/27 16:18
@Author:      CookieYang
@FileName:    MySQLdL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
# import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="13141996jyD@", database="mydatabase", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()