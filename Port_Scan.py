import socket
import sys
import time

try:
	Server = sys.argv[1]
except IndexError:
	Server = input("Server> ")

max_port = 65535
min_port = 1

if(__name__ == "__main__"):
	print("Scansione <" + str(Server) +">")
	
	for port in range(min_port, max_port):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(0.1)
			result = s.connect_ex((Server, port))
			
			if(result == 0):
				#the port is open
				print("Port <" + str(port) + "> is open")
				
			s.close()
		except socket.error as errore:
			print("Errore: " + errore)
		except KeyboardInterrupt:
			print("Scanzione interrotta nella porta <" + str(port) + ">")
			sys.exit()
	
	
	print("Scansione terminata...")
