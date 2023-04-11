# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/11 14:45
@Author:      CookieYang
@FileName:    forms.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User


class RegisterForm(FlaskForm):
    username = StringField('用户名：', validators=[
        DataRequired(), Length(min=6, max=20)])
    email = StringField('邮箱：', validators=[DataRequired(), Email()])
    pwd = PasswordField('密码：', validators=[
        DataRequired(), Length(min=8, max=120)])
    confirm = PasswordField('确认密码：', validators=[
        DataRequired(), EqualTo('pwd')])
    submit = SubmitField('提交')

    def validate_username(self, username):
        user = User.query.filter_by(name=username.data).first()
        if user:
            raise ValidationError("用户昵称已存在。")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('邮箱已存在.')


class LoginForm(FlaskForm):
    username = StringField('用户名：', validators=[
        DataRequired(), Length(min=6, max=20)])
    password = PasswordField('密码：', validators=[DataRequired()])
    submit = SubmitField('登陆')

    def validate_username(self, username):
        user = User.query.filter_by(name=username.data)
        if not user:
            raise ValidationError('用户名不存在。')