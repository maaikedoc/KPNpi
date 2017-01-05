#!/usr/bin/env python

import socket
import string
from gpiozero import LED
from time import sleep
import pygame 

TCP_IP = '192.168.2.148' #IP Address to listen on (Should be external ip for the server)
TCP_PORT = 5005 #Port to listen on
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response, How many characters max should be received per packet

def alarmsound():
        song = "./cow_toy.wav"
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./cow_toy.wav")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10) 

def keuzealarm():
        alarmresp = raw_input("U heeft een alarm notificatie ontvangen. Toets [A] voor bellen, Toets [B] voor luisteren en Toest [C] voor negeren")
        if alarmresp == "a":
                print("Ring ring...")
                ledalarm.off()
                alarmsound()
        elif alarmresp == "b":
                print("Big Brother...")
                ledalarm.off()
        elif alarmresp == "c":
                print("Talk to the hand...")
                ledalarm.off()
        else:
                print("Commando werdt niet herkend. Kies [A], [B] of [C]")
                keuzealarm()


#Catch CTRL + C
conn = False	
s = False
ledalarm = LED(4)
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
			if data=="Huilen!":
                               ledalarm.on()
                               keuzealarm()                                        
			conn.send(data)  # echo
			
except KeyboardInterrupt:
	print 'Closing server...'

	# Close connection if one exists
	if conn:
		conn.close()
	# Close listening server socket
	if s:
		s.close()



