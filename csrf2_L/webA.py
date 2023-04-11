# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/11 10:21
@Author:      CookieYang
@FileName:    webA.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import base64

from flask import Flask, request, render_template, redirect, url_for, make_response
import os
app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


app.secret_key = 'dasdasdsadas'


@app.route('/', methods=["get", "post"])
def index():
    if request.method == 'POST':
        # 取出表单数据
        username = request.form.get("username")
        password = request.form.get("password", "")
        if not all([username, password]):
            print('参数错误')
        else:
            print(username, password)
            if username == 'admin' and password == '1234':
                # 登录成功跳转到转账页面
                response = redirect(url_for('transfer'))
                # 因为转账要求用户登录，所以我们进行状态保持，设置用户名到cookie中
                response.set_cookie('username',username)
                return response
            else:
                print('密码错误')

    return render_template("login2.html")


@app.route('/transfer', methods=["get", "post"])
def transfer():
    # 取出cookie，确保是登录的
    username = request.cookies.get('username', None)
    if not username:
        # 没有代表没登录，跳转到登录页面
        return redirect(url_for('index'))
    if request.method == 'POST':
        to_account = request.form.get("to_account")
        money = request.form.get("money")
        # 取出表单的 crsf_token
        form_crsf_token = request.form.get("crsf_token")
        # 取出 cookie的crsf_token
        cookie_crsf_token = request.cookies.get('crsf_token')
        if form_crsf_token != cookie_crsf_token:
            return "token校验失败,可能是非法操作"
        print('假装执行转账')
        return '转账{}元到{}账户成功！'.format(to_account, money)
    #  使用 make_response, 相当于 django的httpresponse
    # 生成 crsf_token
    crsf_token = generate_crsf()
    response = make_response(render_template('transfer.html', crsf_token= crsf_token))
    # 用于提交验证
    response.set_cookie('crsf_token',crsf_token)
    return response


def generate_crsf():
    return bytes.decode(base64.b64encode(os.urandom(48)))


if __name__ == '__main__':
    app.run(debug=True)