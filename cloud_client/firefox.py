#!/usr/bin/python2

import socket,os,sys,commands,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sip="192.168.10.185"
s_port=8888

os.system('ssh -X test@'+sip+' firefox')


execfile('saas.py')


