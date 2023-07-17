# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/17 15:04
@Author:      CookieYang
@FileName:    urls.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [  # 主页
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
