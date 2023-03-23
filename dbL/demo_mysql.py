# -*- coding: utf-8 -*-
""" 
@Time:        2023/3/23 17:04
@Author:      CookieYang
@FileName:    demo_mysql.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="13141996jyD@",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)