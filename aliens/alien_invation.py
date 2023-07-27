# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/26 18:01
@Author:      CookieYang
@FileName:    alien_invation.py
@SoftWare:    PyCharm
@brief:       功能简介： 启动游戏，资源管理
"""
import pygame
import sys

from setting import Setting
from ship import Ship


class AlienInvation:
    """管理资源"""

    def __init__(self):
        pygame.init()
        self.setting = Setting()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien Invation")

        self.ship = Ship(self)

    def _check_keydowm_events(self, event):
        if event.key == pygame.K_RIGHT:
            print("======right========")
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        """响应键盘和鼠标事件"""
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif event == pygame.KEYDOWN:
                print("key down ...")
                self._check_keydowm_events()
            elif event == pygame.KEYUP:
                self._check_keyup_events()
            elif event == pygame.K_q:
                sys.exit()

    def _update_screen(self):
        # 每次循环时重绘屏幕
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    al = AlienInvation()
    al.run_game()
