# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/28 16:40
@Author:      CookieYang
@FileName:    ActorTcpClient.py
@SoftWare:    PyCharm
@brief:       连接和传递消息以及处理的管理者
"""

from tcpTransClient import tcpTransClient
import dealClientQueueData
import threading
import GV
import time
import class2Json


class ActorTcpClient:
    def __init__(self):
        self.actorTcp = tcpTransClient()

    def startWork(self):
        '''启动TCP'''
        self.actorTcp.run()
        '''启动TCP 客户端处理接收数据'''
        t1 = threading.Thread(target=dealClientQueueData.analysisData, args=())
        t1.start()

    def send(self, data):
        self.actorTcp.m_soc.sendall(data)

    def exit(self):
        '''先退出队列数据处理线程（发送特定paraName的结构体）'''
        time.sleep(1)
        info = class2Json.SubscribeInfo(paraName="EXIT", timeStart=20223, errInfo="I am exit")
        strData = class2Json.wrapCls(info)
        self.send(str(strData).encode())

        '''再退出TCP连接（发送exit)'''
        time.sleep(1)
        self.send(str("exit").encode())
        '''自己退出'''
        #self.actorTcp.close()
        GV.stopAll = True