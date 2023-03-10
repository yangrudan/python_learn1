# -*- coding: utf-8 -*-
"""
@Time:        2022/11/25 16:18
@Author:      CookieYang
@FileName:    ActorTcpServer.py
@SoftWare:    PyCharm
"""
'''
@brief: 
连接和传递消息以及处理的管理者
'''
import tcpTransServer
import dealServerQueueData
import threading
import GV
import time

# '''处理TCP发送队列'''
# def tcpSendDataWork(server):
#     t = threading.current_thread()
#     print("tcpSendDataWork ID is "+ str(t.ident))
#     while True:
#         data = GV.useDataServerSend()
#         if data is None:
#             #print("+++++++++++++++++++++++++++++2")
#             time.sleep(0.1)
#         else:
#             print("send data to client")
#             server.send(data)
'''用上面的方式，报错传参不是iterator,先继承Thread实现'''
class tcpSendWork(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        while True:
            data = GV.useDataServerSend()
            if data is None:
                time.sleep(0.1)
            else:
                print("send data to client")
                self.sock.send(str(data).encode())
            if GV.stopAll == True:
                print("server send thread quit!")
                break




class ActorTcpServer:
    def __init__(self):
        self.actorTcp = tcpTransServer.tcpTransServer()

    def startWork(self):
        '''启动TCP'''
        self.actorTcp.run()
        '''启动TCP 服务器处理接收数据'''
        t1 = threading.Thread(target=dealServerQueueData.analysisData, args=())
        t1.start()

        '''启动TCP 服务器有发送缓冲区数据时进行消息的发送'''
        t2 = tcpSendWork(self.actorTcp.sock)
        t2.start()
        print("ActorTcpServer done")


