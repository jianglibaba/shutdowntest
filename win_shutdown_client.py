# -*- coding: UTF-8 -*-
# 自动关机程序测试版2019.09.17
#Client端部分

import socket    #导入socket模块

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #实例化socket对象
host ='192.168.0.174'

s.connect((host, 9527))  # 与服务端建立通信

cmd = 'shutdown /s /f /t 2' #要执行的dos命令

s.send(cmd.encode("utf8"))   #将dos命令转为bytes传输给服务端