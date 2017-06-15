#!/usr/bin/python

import socket,time,commands,os,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sip="192.168.10.185"
s_port=8888


print "Cloud service loaded, Please enter the authentication details:"
time.sleep(1)

s_user=raw_input("Enter username ") #Taking the username of server as input
s_pass=getpass.getpass("Enter the password ") #Taking the password as input

s.sendto(s_user,(sip,s_port))
s.sendto(s_pass,(sip,s_port))

sdata=s.recvfrom(2)

if sdata[0]=="ok":
	print "Authenticated"
	print "Wait for services"
	time.sleep(2)
	execfile('saas.py')

else:	
	print("Check the username or password again")
	exit()



