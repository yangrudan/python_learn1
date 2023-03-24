# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/25 22:51
@Author:      CookieYang
@FileName:    tcpTransClient.py
@SoftWare:    PyCharm
"""
'''
10.11.125.166', 8082))
OSError: [WinError 10049] 在其上下文中，该请求的地址无效。
10.11.124.1
192.168.0.170
'''
import socket
from threading import Thread
import GV
import class2Json

class RcvTaskHandler(Thread):
    def __init__(self, soc):
        super().__init__()
        self.m_soc = soc

    def run(self):
        while True:
            data = self.m_soc.recv(1024)
            if not data or data.decode('utf-8') == 'exit':
                break
            if GV.stopAll == True:
                print("client rcv run thread quit!")
                break
            print('client rcv: '+data.decode('utf-8'))
            element = class2Json.judgeStrIsSubscribeCls(data)
            if element is None:
                '''abandon data,  do nothing'''
            else:
                print("add server ele -data ......")
                # GV.addDataServer(element)
                GV.addDataClient(data)



class tcpTransClient:
    def __init__(self):
        #  创建客户端
        self.m_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_soc.connect((GV.localIp, 8082))
        self.m_soc.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        self.m_soc.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))

    def send(self, data = 'qq'):
        self.m_soc.send(data.encode())

    def run(self):
        m_task = RcvTaskHandler(soc=self.m_soc)
        m_task.start()#soc=self.m_soc

    def close(self):
        self.m_soc.shutdown(1)
        self.m_soc.close()


'''my test'''
# client = tcpTransClient()
# client.run()
# client.send("qqqq")
# info = class2Json.SubscribeInfo(paraName = "aaa", timeStart= 20223)
# strData = class2Json.wrapCls(info)
# client.send(strData)
