# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/11 14:42
@Author:      CookieYang
@FileName:    __init__.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = '你必须登陆后才能访问该页面'
login_manager.login_message_category = "info"

