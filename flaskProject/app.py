# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/8 13:59
@Author:      CookieYang
@FileName:    app.py
@SoftWare:    PyCharm
@brief:       flask启动器
"""

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/index')
def index():
    places=['北京','上海','广州','深圳','东莞','佛山']
    return render_template('show.html',place=places) #渲染show.html文件并传入place参数

if __name__ == '__main__':
    app.run(port=8080,debug=True)
