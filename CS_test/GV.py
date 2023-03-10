# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/27 10:39
@Author:      CookieYang
@FileName:    GV.py
@SoftWare:    PyCharm
@brief:       存储全局变量
"""


import queue

global localIp
localIp = "127.0.0.1"

global stopAll
stopAll = False

print("~~~~~~~~~~~~~~~this is GV ~~~~~~~~~~~~~~~~~")

#TODO:注意这个buffer不能被其他函数直接使用，后期考虑加锁保护
dataBufferServer = queue.Queue()         #服务器接收队列
dataBufferClient = queue.Queue()         #服务器发送队列
dataBufferServerSend = queue.Queue()     #客户端接收队列
dataBufferClientSend = queue.Queue()     #客户端发送队列



'''
@brief: 
服务器初始化队列
'''
def initBuffServer():
    dataBufferServer.empty()

'''
@brief: 
服务器增加队列元素
'''
def addDataServer(element):
    dataBufferServer.put(element)


'''
@brief:
服务器判断队列非空后取出一个元素
'''
def useDataServer():
    res = None
    if dataBufferServer.empty():
        return res
    else:
        res = dataBufferServer.get()
        return res

####################################################################
'''
@brief: 
服务器初始化发送队列
'''
def initBuffServerSend():
    dataBufferServerSend.empty()

'''
@brief: 
服务器增加tcp发送队列元素
'''
def addDataServerSend(element):
    dataBufferServerSend.put(element)


'''
@brief:
服务器判断发送队列非空后取出一个元素
'''
def useDataServerSend():
    res = None
    if dataBufferServerSend.empty():
        return res
    else:
        res = dataBufferServerSend.get()
        return res
####################################################################
'''
@brief: 
客户端初始化队列
'''
def initBuffClient():
    dataBufferClient.empty()


'''
@brief: 
客户端增加队列元素
'''
def addDataClient(element):
    dataBufferClient.put(element)


'''
@brief:
客户端判断队列非空后取出一个元素
'''
def useDataClient():
    res = None
    if dataBufferClient.empty():
        return res
    else:
        res = dataBufferClient.get()
        return res


####################################################################
'''
@brief: 
客户端初始化发送队列
'''
def initBuffClientSend():
    dataBufferClientSend.empty()


'''
@brief: 
客户端增加发送队列元素
'''
def addDataClientSend(element):
    dataBufferClientSend.put(element)


'''
@brief:
客户端判断发送队列非空后取出一个元素
'''
def useDataClientSend():
    res = None
    if dataBufferClientSend.empty():
        return res
    else:
        res = dataBufferClientSend.get()
        return res