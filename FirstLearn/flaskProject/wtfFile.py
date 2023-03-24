# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/13 15:30
@Author:      CookieYang
@FileName:    wtfFile.py
@SoftWare:    PyCharm
@brief:       Flask-WTF表单提供FileField字段来处理文件上传，它在表单提交后，自动从flask.request.files中抽取数据
"""

import os
from flask import Flask, render_template
from flask_wtf import FlaskForm, CSRFProtect
from flask_wtf.file import FileField, FileRequired, FileAllowed

app = Flask(__name__)
app.config['SECRET_KEY']='hakhfaskh'      #配置CSRF需要的密钥，其值是任意的
csrf = CSRFProtect(app)          #将CSRF保护加入到app中

class Myform(FlaskForm):
    file = FileField(label='用户头像上传',validators=[FileRequired(), FileAllowed(['jpg','png'])])   #创建FileField字段

@app.route('/',methods=['GET','POST'])
def hello_world():
    myform = Myform()         #创建表单对象
    if myform.validate_on_submit():          #检查是否是一个POST请求并且请求是否有效
        filename=myform.file.data.filename    #获取传入的文件名
        filepath=os.path.dirname(os.path.abspath(__file__))       #获取当前项目的文件路径
        savepath=os.path.join(filepath, 'static')      #设置保存文件路径
        myform.file.data.save(os.path.join(savepath,filename))    #保存文件
        return '提交成功'
    return render_template('file.html', myform=myform) #使用render_template()方法渲染file.html文件并将myform传递到file.html中

if __name__ == '__main__':
    app.run(debug=True)