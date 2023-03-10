# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/13 15:40
@Author:      CookieYang
@FileName:    wtfYanzhenMaL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField, CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY']='hakhfaskh' #配置CSRF需要的密钥，其值是任意的
csrf = CSRFProtect(app)     #将CSRF保护加入到app中

class Myform(FlaskForm):
    recaptcha = RecaptchaField() #验证码字段

@app.route('/')
def yanzm():
    myform=Myform()   #创建表单对象
    return render_template('yanzm.html', myform=myform)  #使用render_template()方法渲染yanzm.html文件并将myform传递到file.html中

if __name__ == '__main__':
    app.run()