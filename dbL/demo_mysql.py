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

# 插入表
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

"""
# 元组插入
"""
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
"""
# 插入一行并返回ID
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
"""

# SELECT 选取
"""
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
"""