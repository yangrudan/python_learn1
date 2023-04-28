# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/11 14:43
@Author:      CookieYang
@FileName:    models.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from SecondLearn.LOGINl import db, login_manager
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    # __table_args__ = {"useexisting": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    pwd = db.Column(db.String(120), nullable=False)

    things = db.relationship('Thing', backref='User', lazy='dynamic')

    def __repr__(self):
        return "<User %r>" % self.name

    def generate_password_hash(self, pwd):
        self.pwd = generate_password_hash(pwd)

    def check_password_hash(self, pwd):
        return check_password_hash(self.pwd, pwd)


class Thing(db.Model):
    __tablename__ = 'things'
    # __table_args__ = {"useexisting": True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    add_date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "<Todo %r>" % self.id