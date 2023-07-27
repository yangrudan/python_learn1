# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/26 18:12
@Author:      CookieYang
@FileName:    setting.py
@SoftWare:    PyCharm
@brief:       功能简介: 修改游戏的外观和行为
"""


class Setting:
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
