# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/28 10:35
@Author:      CookieYang
@FileName:    dealClientQueueData.py
@SoftWare:    PyCharm
"""
import GV
import time
import class2Json

###############################处理Rcv Buffer start#####################################
def caseSubscribeType(ele : class2Json.SubscribeInfo):
    if ele.paraName == "EXIT":
        GV.stopAll = True
    else:
        print("~~~~~~~~client analysis add ele send!!!!!!!!!!!")
        '''收到消息直接处理即可'''
        # srvSendInfo = class2Json.SubscribeInfo(paraName="I rcved", timeStart=20221128)
        # strData = class2Json.wrapCls(srvSendInfo)
        # GV.addDataServerSend(strData)


def analysisData():
    while True:
        data = GV.useDataClient()
        if data is None:
            time.sleep(0.1)
        else:
             ele = class2Json.str2Cls(data)
             #没加错误判断，加入队列时已进行符合要求的数据校验
             caseSubscribeType(ele)
        if GV.stopAll == True:
            print("client Analysis Thread quit!")
            break

###############################处理Rcv Buffer end#####################################
'''发送队列的处理要结合tcp client对象，放在ActorTCpClient里统一管理'''