# -*- coding: UTF-8 -*-
# 自动关机程序测试版2019.09.17
# Client端部分

import socket
import shutdownlog, os

log_file = 'shutdownlog.txt'


def winclose(hostw):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hostw, 9527))
        cmd = 'shutdown /s /f /t 2'
        s.send(cmd.encode("utf8"))
        shutdownlog.succeed(hostw, log_file)
    except:
        shutdownlog.false(hostw, log_file)


def linuxclose(hostl):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hostl, 9527))
        cmd = 'shutdown now'
        s.send(cmd.encode("utf8"))
        shutdownlog.succeed(hostl, log_file)
    except:
        shutdownlog.false(hostl, log_file)


if not os.path.exists(log_file):
    f = open(log_file, 'w')
    f.write('自动关机日志：\n')
    f.flush()
    f.close()

wf = open('winclose.txt', 'r')
for wline in wf.readlines():
    wline = wline.strip('\n')
    winclose(wline)
wf.close()

lf = open('linuxclose.txt', 'r')
for lline in lf.readlines():
    lline = lline.strip('\n')
    linuxclose(lline)
lf.close()

#ip ='192.168.0.9'
#try:
#    os.system('shutdown /s /f /t 2')
#    shutdownlog.succeed(ip, log_file)
#except:
#    shutdownlog.false(ip, log_file)
