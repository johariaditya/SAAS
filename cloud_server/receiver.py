#!/usr/bin/python2

import socket,os,sys,commands
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))

cdata=s.recvfrom(100)
cdata1=s.recvfrom(100)

if cdata[0]=="test" and cdata1[0]=="123":
	s.sendto("ok",cdata[1])
else:
	s.sendto("not ok",cdata[1])


