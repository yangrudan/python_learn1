# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/25 17:01
@Author:      CookieYang
@FileName:    serverTcp.py
@SoftWare:    PyCharm
@brief：      最简单的例子
"""
import socket
import threading
import time

#  创建socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  监听端口
#  soc.bind(('192.168.43.141', 8087))
soc.bind(('192.168.0.170', 8081))
# listen()方法开始监听端口，传入的参数指定等待连接的最大数量
soc.listen(5)
print('waiting for connection...')


def Tcplink(sock, addr):
    print('Accept new connection form %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Have Received: %s!' % data.decode('utf-8')).encode('utf-8'))
        #  sock.close()
        print('Connection from %s Received: %s  ' % addr, data)


while True:
    #  接受一个新连接：
    sock, addr = soc.accept()
    #  创建新线程来处理连接

    t = threading.Thread(target=Tcplink(sock, addr), args=(sock, addr))
    t.start()
    data = sock.recv(1024)
    time.sleep(1)
    if not data or data.decode('utf-8') == 'exit':
        break