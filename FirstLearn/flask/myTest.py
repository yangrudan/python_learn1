# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/2 17:11
@Author:      CookieYang
@FileName:    myTest.py
@SoftWare:    PyCharm
@brief:       尝试使用Flask
"""

from flask import *

app=Flask(__name__,static_url_path='/s',static_folder='/static')

@app.route('/')      #设置根目录路由
def hello():
    return '<h1>hello world</h1>'
@app.route('/<string:id>')
def type(id):
    if id=='s':
        return 'python'
    if id=='ss':
        return 'java'
    if id=='sss':
        return 'C++'


@app.route('/index',methods=['GET','POST'])    #获取表单（模板）并渲染
def index():
    if(request.method=='GET'):
        return render_template('index.html')
    elif(request.method=='POST'):
        name=request.form.get("name")
        password=request.form.get("key")

        print(name,password)
        return "Get the post"

if __name__ == '__main__':
    app.run()

