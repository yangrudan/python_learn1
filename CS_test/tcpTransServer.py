# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/25 19:13
@Author:      CookieYang
@FileName:    tcpTransServer.py
@SoftWare:    PyCharm
"""
import socket
import threading
import time
import GV
import class2Json
import logging

logging.disable(logging.DEBUG)
logging.basicConfig(level= logging.CRITICAL, format='%(asctime)s -%(levelname)s -%(message)s')


def Tcplink(sock, addr):
    print('Accept new connection form %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        try:
            data = sock.recv(1024)
            time.sleep(0.1)
            if not data or data.decode('utf-8') == 'exit':
                print("exit server TCPlink")
                break
            element = class2Json.judgeStrIsSubscribeCls(data)
            if element is None:
                '''abandon data,  do nothing'''
            else:
                print("add server ele -data ......")
                # GV.addDataServer(element)
                GV.addDataServer(data)

            # sock.send(('Have Received: %s!' % data.decode('utf-8')).encode('utf-8'))
            print('Connection from %s Received: %s  ' % addr, data)
        except Exception as err:
            logging.critical(err)
            break

'''
#获得的地址不正确
import requests
r = requests.get('http://myip.ipip.net', timeout=6).text
print(r)
'''
class tcpTransServer:
    def __init__(self):
        #  创建socket
        self.m_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #  监听端口
        self.m_soc.bind((GV.localIp, 8082))
        # listen()方法开始监听端口，传入的参数指定等待连接的最大数量
        self.m_soc.listen(5)
        print('waiting for connection...')
        self.m_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.m_soc.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        # self.m_soc.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))
        #TODO: Queue放在这里有一些奇怪，暂时没想到放在其他地方方法
        #队列初始化
        GV.initBuffServer()
        GV.initBuffServerSend()

    def run(self):
        while True:
            #  接受一个新连接：
            self.sock, \
            self.addr = self.m_soc.accept()
            #  创建新线程来处理连接

            t = threading.Thread(target=Tcplink, args=(self.sock, self.addr))
            t.start()
            #print("before break ----")
            break #yrd add
            data = self.sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
        print("!!!server socket listen quit!!!!!!!!!!")

    def send(self, data):
        self.sock.send(data)


'''my test'''
# t = threading.current_thread()
# print('~~~~~~~~~~~~Main Thread id : %d' % t.ident)
# server = tcpTransServer()
# server.run()
#
# print("start========")
# time.sleep(16)
# server.send(b"dd")
# print("stop========")
