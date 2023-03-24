# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/19 10:56
@Author:      CookieYang
@FileName:    sendEmail.py
@SoftWare:    PyCharm
@brief:       SMTP简单邮件传输协议
"""
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = '1549029765@qq.com'
    receivers = ['1549029765@qq.com', 'xy6617@qq.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('yangyang', 'utf-8')
    message['To'] = Header('xuxu', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'kfsojfnomfoxgage')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()