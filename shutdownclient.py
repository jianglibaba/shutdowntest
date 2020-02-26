# -*- coding: UTF-8 -*-
# 自动关机程序测试版2019.09.17
# Client端部分

import socket  # 导入socket模块
import shutdownlog, os,time

log_file = 'shutdownlog.txt'


def winclose(hostw):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket对象
        s.connect((hostw, 9527))  # 与服务端建立通信
        cmd = 'shutdown /s /f /t 2'  # 要执行的dos命令
        s.send(cmd.encode("utf8"))  # 将dos命令转为bytes传输给服务端
        shutdownlog.succeed(hostw, log_file)    #成功记录日志
    except:
        shutdownlog.false(hostw, log_file)  ##失败记录日志


def linuxclose(hostl):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket对象
        s.connect((hostl, 9527))  # 与服务端建立通信
        cmd = 'shutdown now'  # 要执行的shell命令
        s.send(cmd.encode("utf8"))  # 将shell命令转为bytes传输给服务端
        shutdownlog.succeed(hostl, log_file)
    except:
        shutdownlog.false(hostl, log_file)


if not os.path.exists(log_file):
    f = open(log_file, 'w')
    f.write('自动关机日志：\n')
    f.flush()
    f.close()

f = open('winclose.txt', 'r')  # 打开win主机地址列表
for line in f.readlines():  # 每行每行遍历
    line = line.strip('\n')  # 去掉换行符
    winclose(line)  # 执行win关机函数
f.close()

f = open('linuxclose.txt', 'r')
for line in f.readlines():
    line = line.strip('\n')
    linuxclose(line)
    time.sleep(60) #每次休眠60秒
f.close()

ip ='192.168.0.9'
try:
    os.system('shutdown /s /f /t 2')    #本机关机
    shutdownlog.succeed(ip, log_file)
except:
    shutdownlog.false(ip, log_file)
