#!/usr/bin/python2

import socket,os,sys,commands,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sip="192.168.122.240"
s_port=8888

os.system("SSHPASS='123' sshpass -e ssh -X test@"+sip+" cheese ")
time.sleep(3)

execfile('saas.py')


