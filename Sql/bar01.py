# -*- coding: utf-8 -*-
""" 
@Time:        2023/3/26 22:09
@Author:      CookieYang
@FileName:    bar01.py
@SoftWare:    PyCharm
@brief:       功能简介
"""

# 1.导包
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/testDB"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class sheets(db.Model):
    __tablename__ = "bar01"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer())


# 使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上。
# 处理URL和视图函数的关系的程序就是路由，这里的视图函数就是index。
@app.route("/")
def index():
    sheets_list = sheets.query.all()
    # 说白了，其实render_template的功能是对先引入index.html，
    # 同时根据后面传入的参数，对html进行修改渲染  --- 处理数据
    return render_template("bar01.html", sheets=sheets_list)


if __name__ == '__main__':
    ctx = app.app_context()
    ctx.push()
    db.drop_all()  # 若有表先清除
    db.create_all()  # 创建表

    c1 = sheets(name="a", age=18)  # 编写数据
    c2 = sheets(name="b", age=22)
    c3 = sheets(name="c", age=20)
    c4 = sheets(name="e", age=17)
    c5 = sheets(name="f", age=23)
    c6 = sheets(name="g", age=15)

    db.session.add_all([c1, c2, c3, c4, c5, c6])  # 向表中插入数据
    db.session.commit()  # 利用session进行提交
    app.run(debug=True)  # 运行
