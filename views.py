# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/11 14:48
@Author:      CookieYang
@FileName:    views.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from SecondLearn.LOGINl import app, db
from forms import RegisterForm, LoginForm
from models import User


@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


@app.route('/')
@app.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('index.html', title="首页")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data
        user = User.query.filter_by(name=name).first()
        if user and user.check_password_hash(pwd):
            login_user(user)
            flash('登陆成功。', category='info')
            return redirect(url_for('index'))
        else:
            flash("密码或账户错误。", category='error')
    return render_template('login.html', title='登录', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('再见！')
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        pwd = form.pwd.data
        user = User(name=username, email=email)
        user.generate_password_hash(pwd)
        db.session.add(user)
        db.session.commit()
        flash('注册成功', category='info')
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)