#!/usr/bin/python2

import os,time,commands,sys,socket

x="""
Press 1 to get Firefox  :
Press 2 to get vlc      :
Press 3 to open calculator:
Press 4 to open office   :
Press 5 to take a screenshot  :
Press 6 to to start the webcam      :

"""
print x

ch=raw_input()

if ch=='1':
	print "Now wait for a second"
	execfile('firefox.py')

if ch=='2':
	print "Now wait for a second"
	execfile('vlc.py')

if ch=='3':
	print "Now wait for a second"
	execfile('calculator.py')

if ch=='4':
	print "Now wait for a second"
	execfile('office.py')

if ch=='5':
	print "Now wait for a second"
	execfile('screenshot.py')

if ch=='6':
	print "Now wait for a second"
	execfile('webcam.py')

else:
	print "wrong option"

