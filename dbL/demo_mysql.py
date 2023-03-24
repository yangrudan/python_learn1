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
  auth_plugin='mysql_native_password',
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")  # 创建数据库

# mycursor.execute("SHOW DATABASES")  # 检查数据库

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")  # 创建表

# mycursor.execute("SHOW TABLES")  # 返回数据库列表

# Table 'customers' already exists 创建表时创建主键
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

"""