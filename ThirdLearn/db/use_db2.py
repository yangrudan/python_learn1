"""
Copyright (c) Zhejiang Lab. All right reserved.
"""


from manipulate_db import SqliteTool

db_id = 0   # 需要自己维护

db = SqliteTool()

db.create_tabel('''CREATE TABLE if not exists CONSUMPTION
       (ID            INTEGER PRIMARY KEY     AUTOINCREMENT,
       TYPE           TEXT                    NOT NULL,
       DESC           TEXT,
       DATE           TEXT                    NOT NULL,
       MONEY          REAL);''')


# 添加数据
a_record = ('水果', "orange",'2023-11-08', 0.00)
db.operate_one("""INSERT INTO CONSUMPTION (TYPE, DESC, DATE, MONEY) VALUES (?, ?, ?, ?)""", a_record)

# 查询数据
select_sql = "select * from CONSUMPTION where DESC =:mydesc"
r = db.query_many(select_sql, {"mydesc": 'apple'})
print(r)

# 按时间查询数据
start_date = "2023-08-06"
end_date = "2023-09-09"
select_sql = "SELECT * FROM CONSUMPTION WHERE DATE BETWEEN '{}' AND '{}'".format(start_date, end_date)
r = db.query_many(select_sql)
print(r)

# 更新数据
update_sql = "UPDATE CONSUMPTION SET MONEY = ? WHERE TYPE = ? AND DESC=? AND DATE=?"
place = (1.0, '水果', 'apple', '2023-08-08')
db.operate_one(update_sql, place)

# 删除数据
del_sql = "DELETE FROM CONSUMPTION WHERE TYPE = ? AND DESC=? AND DATE=?"
place = ("水果","apple","2023-08-08")
db.operate_one(del_sql, place)


db.close_con()

