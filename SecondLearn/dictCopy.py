# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/18 13:50
@Author:      CookieYang
@FileName:    dictCopy.py
@SoftWare:    CLion
@brief:       功能简介
"""
aliens = []
new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
for alien_number in range(10):
    aliens.append(dict(new_alien))
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['points'] = 10
        alien['speed'] = 'fast'
print(aliens)
