# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/13 9:17
@Author:      CookieYang
@FileName:    mailL.py
@SoftWare:    PyCharm
@brief:       POP3:kfsojfnomfoxgage    SMTP:hndhnrfmvcjjifjf
"""
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'  # 邮件服务器的名称/IP地址
app.config['MAIL_PORT'] = 465  # 所用服务器的端口号
app.config['MAIL_USERNAME'] = '1549029765@qq.com'  # 发件人的用户名
app.config['MAIL_PASSWORD'] = 'kfsojfnomfoxgage'  # 发件人的POP3/IMAP/SMTP服务的SSL连接客户端授权码
app.config['MAIL_USE_TLS'] = False  # 禁用传输安全层加密
app.config['MAIL_USE_SSL'] = True  # 启用安全套接字层加密
mail = Mail(app)  # 创建邮件类对象


@app.route('/write')
def write_mail():
    return render_template('write.html')


@app.route('/send', methods=['GET', 'POST'])
def send_mail():
    username = request.form.get('username')  # 获取请求中的username参数
    theme = request.form.get('theme')  # 获取请求中的theme参数
    content = request.form.get('content')  # 获取请求中的content
    msg = Message(theme, sender='1549029765@qq.com', recipients=[username], body=content)  # 使用Messgae方法
    mail.send(msg)  # 使用Mail类中的send()方法
    return '邮件发送成功'


if __name__ == '__main__':
    app.run(debug=True)
