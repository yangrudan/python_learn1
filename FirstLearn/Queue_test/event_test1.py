# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/6 14:37
@Author:      CookieYang
@FileName:    event_test1.py
@SoftWare:    PyCharm
@brief:       不要用时间控制，wait之后使用clear
"""

import threading,time

class Player(threading.Thread):
    def __init__(self, name, e_pre, e_self):
        threading.Thread.__init__(self)
        self.name = name
        self.e_pre = e_pre
        self.e_self = e_self
        self.count = 0

    def run(self):
        while self.count < 3:
            self.count += 1
            time.sleep(0)
            self.e_pre.wait()
            self.e_pre.clear()

            print('%s 第%d次操作===>' % (self.name, self.count))
            time.sleep(0)
            self.e_self.set()
        time.sleep(0.1)
        print('%s Done!' % self.name)

# a,b,c用户，分别对于三个event,负责通知下一个用户操作
a_event = threading.Event()
b_event = threading.Event()
c_event = threading.Event()
# 操作顺序: a -> b -> c
# 通知操作: c_event -> a ; a_event -> b; b_event ->c

a = Player('A', c_event, a_event)
b = Player('B', a_event, b_event)
c = Player('C', b_event, c_event)

for i in [a, b, c]:
    i.start()

# 延时要配置好，要不，输出顺序会乱
time.sleep(0)
# 最开始是由a出牌
# b_event.set()
c_event.set()

for i in [a, b, c]:
    i.join()

print('-'*15)