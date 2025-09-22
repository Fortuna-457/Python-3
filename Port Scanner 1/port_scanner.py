#!/usr/bin/env python3

"""Simple port scanner script."""

__version__ = "1.0.0"

import socket

host = '192.168.18.1'
port = 29

def port_scanner(port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	
	# En condicionales 0 vale false
	if s.connect_ex((host, port)):
		print(f"\n[!] El puerto {port} está cerrado")
	else:
		print(f"\n[+] El puerto {port} está abierto")

	s.close()

def main():
	port_scanner(port)

if __name__=='__main__':
	main()