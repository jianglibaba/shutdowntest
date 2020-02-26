#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 自动关机程序测试版2019.09.17
#Linux_Server端部分

import socket,subprocess    #导入socket模块和命令行交互模块

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #实例化socket对象

s.bind(("192.168.0.177",9527))
#建立服务端的绑定信息服务IP是192.168.0.177,端口号是9527

s.listen(5) #建立监听,后备链接最大值为5

while True:
    client,clientip = s.accept()    #等待客户端的连接...并获得连接句柄client
    cmd = client.recv(1024)    #接收客户端传来的bytes数据
    Res = subprocess.run(cmd.decode("utf8"), shell=True)
    # 实例化subprocess对象,执行由客户端发来的命令
    client.close()
s.close()

