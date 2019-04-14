#!/usr/bin/python 

import socket #import socket module

s = socket.socket() #create a socket object
print "socket made"

host = '10.98.76.121' #Host i.p
port = 12397 #Reserve a port for your service

print "before connect"
s.connect((host,port))
print "after connect"
print s.recv(1024)
s.close