# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/28 9:38
@Author:      CookieYang
@FileName:    mainServer.py
@SoftWare:    PyCharm
"""
'''
1. 暂时定为SubscribeInfo的参数paraName为EXIT是退出, GV.stopAll进行全局控制

'''
import ActorTcpServer

if __name__ == '__main__':
    myServerActor = ActorTcpServer.ActorTcpServer()
    myServerActor.startWork()
