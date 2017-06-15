#!/usr/bin/python2

import os,time,commands,sys,socket

x="""
Press 1 to get Firefox  :
Press 2 to get vlc      :
Press 3 to get calculator:
Press 4 to get office   :

"""
print x

ch=raw_input()

if ch=='1':
	print "Now wait for a second"
	execfile('firefox.py')

else:
	print "wrong option"

