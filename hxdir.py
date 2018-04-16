#!/usr/bin/python

import requests
import sys,time
import multiprocessing


def genlist(file):
	f = open(file,"r")
	g3n = f.read().split("\n")
	return g3n

def main(url,files):
	req = requests.get(url+files+".php")

	if req.status_code == 200:
		print "FOUND : ",url +files+".php"
		x = open("found.txt","a")
		x.write(url+files+"\n")
		x.close()

if __name__ == '__main__':
	try:
		file1 = genlist(sys.argv[2])
		rez = []
		for i in file1:
			time.sleep(0.1)
			p = multiprocessing.Process(target=main,args=(sys.argv[1],i))
			rez.append(p)
			p.start()
	except:
		print "Something Wrong .."
		pass




