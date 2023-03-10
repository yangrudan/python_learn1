# -*- coding: utf-8 -*-
"""
@Time:        2022/11/28 10:35
@Author:      CookieYang
@FileName:    dealServerQueueData.py
@SoftWare:    PyCharm
@brief:       判断队列的数据进行处理(对接收队列进行解析)
"""
import GV
import time
import class2Json
import logging


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s  -%(message)s')
###############################处理Rcv Buffer start#####################################
def caseSubscribeType(ele : class2Json.SubscribeInfo):
    if ele.paraName == "EXIT":
        print("server analysis thread ready quit!")
        GV.stopAll = True
    else:
        print("~~~~~~~~analysis add ele send")
        srvSendInfo = class2Json.SubscribeInfo(paraName="I rcved", timeStart=20221128)
        strData = class2Json.wrapCls(srvSendInfo)
        GV.addDataServerSend(strData)
        logging.debug("add a message2 tcp server send buff")


def analysisData():
    while True:
        data = GV.useDataServer()
        if data is None:
            time.sleep(0.1)
        else:
             ele = class2Json.str2Cls(data)
             #没加错误判断，加入队列时已进行符合要求的数据校验
             caseSubscribeType(ele)
             print("analysis rcv data========")
        if GV.stopAll == True:
            print("server analysis data quit!")
            break
###############################处理Rcv Buffer end#####################################
'''发送队列的处理要结合tcp server对象，放在ActorTCpServer里统一管理'''