# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/26 18:22
@Author:      CookieYang
@FileName:    ship.py
@SoftWare:    PyCharm
@brief:       功能简介: 负责飞船的大部分行为
"""
import pygame


class Ship:
    def __init__(self, al_game):
        self.screen = al_game.screen
        self.setting = al_game.setting
        self.screen_rect = al_game.screen.get_rect()

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/universe_ship.bmp')
        self.rect = self.image.get_rect()

        # 每艘新飞船都zhi于屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数数值
        self.x = float(self.rect.x)

        # 持续移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            print("Ship update right")
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        # 根据self.x更新rect对象
        self.rect.x = self.x

