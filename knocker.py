import socket
import time
import sys


open_p = [1010,1011,1012]
close_p = [1012,1011,1010]

host = sys.argv[1]

def knocker(mode):
	if mode == "open":
		for i in open_p:
			try:
				s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				s.connect((host,i))
				time.sleep(1)
			except:
				print("[+] knock knock at : %d")%i
		print("[*] Service OPENED ^_^ ")
	elif mode == "close":
                for i in close_p:
                        try:
                                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                                s.connect((host,i))
                                time.sleep(1)
                        except:
                                print("[+] knock knock at : %d")%i
            	print("[-] Service CLOSED >_< ")
knocker(sys.argv[2])
