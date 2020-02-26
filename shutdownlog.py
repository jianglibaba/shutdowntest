# -*- coding: UTF-8 -*-
import time

def succeed(host,log_file):
        logtime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        logline ='%s\t%s 成功关机。\n' %(logtime,host)
        f =open(log_file,'a')
        f.write(logline)
        f.flush()
        f.close()


def false(host, log_file):
    logtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    logline = '%s\t%s 关机失败，请检查！\n' %(logtime,host)
    f = open(log_file, 'a')
    f.write(logline)
    f.flush()
    f.close()

