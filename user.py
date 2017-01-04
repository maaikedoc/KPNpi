#!/usr/bin/env python

import socket


TCP_IP = '130.89.130.185' #IP Address to listen on (Should be external ip for the server)
TCP_PORT = 5005 #Port to listen on
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response, How many characters max should be received per packet

#Catch CTRL + C
conn = False	
s = False
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT)) #Create the server socket
	s.listen(1) # Start listening on serversocket for open connections

	while True:

		conn, addr = s.accept() #Accept a single connection and do stuff with it
		print 'Connection address:', addr
	
		while 1:
			try:
				data = conn.recv(BUFFER_SIZE) #Receive maximum of BUFFER_SIZE characters in data
				if len(data) == 0:
					break;
			except socket.error:
				break;
			print "received data:", data
			conn.send(data)  # echo
except KeyboardInterrupt:
	print 'Closing server...'

	# Close connection if one exists
	if conn:
		conn.close()
	# Close listening server socket
	if s:
		s.close()
