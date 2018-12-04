import socket
import sys
import time

####################################################
# in queste due funzioni implementiamo la creazione di un file
# in cui verranno memorizzate tutte le info della scansione
def create_file(server_address):
	f = open(str(server_address) + ".txt", "w")
	f.write("Scansione del server: " + server_address)
	f.write("\nScansione effettuata il: " + time.ctime() + "\n")
	f.close()

def write_port(server_address, port):
	f = open(server_address + ".txt", "a")
	f.write("\nPort <" + str(port) + " is open.")
	f.close()
######################################################à

max_port = 65535
min_port = 1
list_of_ports = []


if(__name__ == "__main__"):
	try:
		Server = sys.argv[1]
	except IndexError:
		Server = input("Server> ")

	create_file(Server)

	print("\n[+] Scansione <" + str(Server) +">")
	
	for port in range(min_port, max_port):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(0.1)  #timeout fra una scansione e un altra in secondi
			result = s.connect_ex((Server, port))
			
			if(result == 0):
				#the port is open
				list_of_ports.append(port)
				print("Port <" + str(port) + "> is open")
				write_port(Server, port)
				
			s.close()
		except socket.error as errore:
			print("Errore: " + errore)
		except KeyboardInterrupt:
			message = "\n\nScanzione interrotta nella porta <" + str(port) + ">"
			print(message)
			f = open(Server + ".txt", "a")
			f.write(message)
			f.close()
			sys.exit()
	
	
	print("Scansione terminata...\nRisultati:")
	print(list_of_ports)
