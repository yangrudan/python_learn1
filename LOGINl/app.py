# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/4 15:18
@Author:      CookieYang
@FileName:    app.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore, \
    UserMixin, RoleMixin, login_required, auth_token_required, http_auth_required
from sqlalchemy import create_engine, Boolean, DateTime, \
    Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# 创建flask应用
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_TRACKABLE'] = True
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///security-dev.sqlite'
app.config['SECURITY_PASSWORD_SALT'] = '951623847'
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'

# 创建数据库连接
engine = create_engine('sqlite:///test.db', \
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# 创建数据库
def init_db():
    Base.metadata.create_all(bind=engine)

# 创建模型
class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))

# 设置flask-security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

# 创建测试用户
@app.before_first_request
def create_user():
    try:
        db_session.query(User).first()
    except:
        print('初始化数据库')
        init_db()
        print('创建用户')
        user_datastore.create_user(username='yang', password='123456')
        print('提交数据')
        db_session.commit()

# 创建视图
@app.route('/')
@login_required
def home():
    return 'you\'re logged in!'

@app.route('/api')  #
@http_auth_required
@auth_token_required
def token_protected():
    return 'you\'re logged in by Token!'

if __name__ == '__main__':

    app.run()