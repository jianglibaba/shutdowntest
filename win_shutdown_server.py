# -*- coding: UTF-8 -*-
# 自动关机程序测试版2019.09.17
# Win_Server端部分

import socket,subprocess

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("192.168.0.11",9527))

s.listen(5)

while True:
    client, clientip = s.accept()
    cmd = client.recv(1024)
    Res = subprocess.run(cmd.decode("utf8"), shell=True)
    client.close()

