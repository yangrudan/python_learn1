# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/12 16:34
@Author:      CookieYang
@FileName:    cacheL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from flask import Flask
from flask_caching import Cache
import time
#配置RedisCache缓存类型参数值，我们使用本地的redis，没有密码
config={
    'CACHE_TYPE':'redis',  #使用redis作为缓存
    'CACHE_REDIS_HOST':'127.0.0.1',  #redis地址
    'CACHE_REDIS_PORT':6379  #redis端口号
}


app = Flask(__name__)


#初始化缓存
cache=Cache(app=app,config=config)  #创建Cache对象
#或使用init_app()初始化缓存
#cache=Cache()         #创建Cache对象
#cache.init_app(app=app,config=config)


@app.route('/view')
@cache.cached(timeout=30)  #设置超时时间
def view():
    time.sleep(2)       #模拟数据加载时间
    return '视图函数缓存'

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()