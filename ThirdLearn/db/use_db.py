"""
Copyright (c) Zhejiang Lab. All right reserved.
"""

import sqlite3

# 连接数据库，如果不存在则创建数据库
conn = sqlite3.connect('test.db')


# 创建新表
conn.execute('''CREATE TABLE if not exists CONSUMPTION
       (ID            INT PRIMARY KEY          NOT NULL,
       TYPE           TEXT                     NOT NULL,
       DESC           TEXT,
       DATE           TEXT                    NOT NULL,
       MONEY          REAL);''')
conn.commit()


# 插入一条记录
conn.execute("""INSERT INTO CONSUMPTION (ID,TYPE,DESC,DATE,MONEY) \
      VALUES (2, '水果', "apple",'2023-08-06', 0.00)""")
conn.commit()

# # 插入多条记录
# conn.executemany("INSERT INTO CONSUMPTION (ID,TYPE,DESC,DATE,ADDRESS,MONEY) \
#               VALUES (?, ?, ?, ?, ?, ?)", \
#                  [(2, '出行', "", 2023-08-09, '杭州', 0.00), \
#                   (3, '早点', '', 2023-08-09, '杭州', 0.00), \
#                   (4, '零食', '', 2023-08-09, '杭州', 0.00)])
# conn.commit()
#
#
# # 插入多条记录
# conn.executemany("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#               VALUES (?, ?, ?, ?, ?)", \
#                  [(2, 'Allen', 25, 'Texas', 15000.00), \
#                   (3, 'Teddy', 23, 'Norway', 20000.00), \
#                   (4, 'Mark', 25, 'Rich-Mond', 65000.00)])
# conn.commit()


conn.close()
#关闭连接，更新数据库文件