#!/usr/bin/python

from pwn import *
import sys
import os

def connect2ssh(username,pwd):
	con2ssh = ssh(host=sys.argv[1],user=username,password=pwd,port=int(sys.argv[2]))
	cn = con2ssh.process(argv=["id"])
	print cn.recv()

def cp2ssh(filen,host,username,path):
	cmd = "scp %s %s@%s:%s"%(filen,username,host,path)
	print cmd

