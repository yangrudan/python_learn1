# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/28 9:39
@Author:      CookieYang
@FileName:    mainClient.py
@SoftWare:    PyCharm
"""

import ActorTcpClient
import class2Json


if __name__ == '__main__':
    myClientActor = ActorTcpClient.ActorTcpClient()
    myClientActor.startWork()
    myClientActor.send(str("qqqq").encode())
    info = class2Json.SubscribeInfo(paraName="aaa", timeStart=20223, errInfo="I am fine")
    strData = class2Json.wrapCls(info)
    myClientActor.send(str(strData).encode())
    '''退出线程请求'''
    myClientActor.exit()



