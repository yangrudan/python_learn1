# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/25 17:01
@Author:      CookieYang
@FileName:    clientTcp.py
@SoftWare:    PyCharm
@brief：      最简单的例子
"""
import socket
import time

#  创建客户端
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  连接
#  soc.connect(('192.168.43.141', 8087))
soc.connect(('192.168.0.170', 8081))
send_data = input("请输入要发送客户端的测试数据:")
soc.send(send_data.encode())
time.sleep(5)
print(soc.recv(1024).decode('utf-8'))
for data in [b'mary', b'bob', b'jack']:
    #   发送数据
    soc.send(data)
    print(soc.recv(1024).decode('utf-8'))
soc.send(b'exit')
#  套字节关闭
soc.close()