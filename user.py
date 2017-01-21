#!/usr/bin/env python

import socket
import string
from gpiozero import LED
import time
import pygame #audio
import RPi.GPIO as GPIO #push button
import sys

TCP_IP = '192.168.1.72' #IP Address to listen on (Should be external ip for the server)
TCP_PORT = 5005 #Port to listen on
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response, How many characters max should be received per packet
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Define GPIO pins
ledalarm = LED(4)
ledmove = LED(17)
ledsocial = LED(27)
ledwander = LED(22)
ledeat = LED(18)
call = GPIO.input(26)
listen = GPIO.input(19)
stop = GPIO.input(13)

#ALARMCHOICE DEFINITIONS TRUE
#Define all the audio functions needed to run the alarm call - true
def callsound():
        song = "./Music/dial.mp3"
        print("Ring, ring...")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/dial.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm1woman():
        song = "./Music/28.wav"
        print("Help, help")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/28.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm1man():
        song = "./Music/1.mp3"
        print("Wat is er gebeurd?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/1.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def alarm2woman():
        song = "./Music/29.wav"
        print("Ik ben gevallen")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/29.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm2man():
        song = "./Music/2.mp3"
        print("Moet ik een ambulance bellen?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/2.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm3woman():
        song = "./Music/30.wav"
        print("Ja, het doet heel veel pijn")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/30.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm3man():
        song = "./Music/3.mp3"
        print("Ik bel een ambulance en kom nu naar huis!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/3.mp3")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

def alarmwomanlisten1():
        song = "./Music/34.wav"
        print("Help, help! Is daar iemand? Hallo?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/34.wav")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

#alarm call true - call 
def alarmcall1():
                print("Call subject true alarm")
                ledalarm.off()
                callsound()
                alarm1woman()
                alarm1man()
                alarm2woman()
                alarm2man()
                alarm3woman()
                alarm3man()
                sentinal()

#alarm call true - listen
def alarmlisten1():
                print("Listen to subject true alarm")
                ledalarm.off()
                alarmwomanlisten1()
                sentinal()

#make choice when true alarm is called                
def alarmtrue():
        while True:
                call = GPIO.input(26)
                listen = GPIO.input(19)
                stop = GPIO.input(13)
                if call == False:
                        print('Call')
                        alarmcall1()
                elif listen == False:
                        print("Listen")
                        alarmlisten1()
                elif stop == False:
                        print("Stop")
                        sentinal()
                        
#ALARMCHOICE DEFINITIONS FALSE
#define all the audio functions needed to run the alarm call - false
def alarm4woman():
        song = "./Music/32.wav"
        print("*serie en gelach op de achtergrond*")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/32.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm4man():
        song = "./Music/4.mp3"
        print("Had je net om hulp geroepen?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/4.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm5woman():
        song = "./Music/18.wav"
        print("Oh haha nee, ik liet net iets vallen, maar alles gaat goed hier!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/18.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm5man():
        song = "./Music/5.mp3"
        print("Oke, ik zie je straks!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/5.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarm6woman():
        song = "./Music/19.wav"
        print("Tot straks en nog veel plezier!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/19.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def alarmwomanlisten2():
        song = "./Music/33.wav"
        print("*Serie speelt op achtergrond met gelach*")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/33.wav")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
                
#alarm call false - call
def alarmcall2():
                print("Call subject false alarm")
                ledalarm.off()
                callsound()
                alarm4woman()
                alarm4man()
                alarm5woman()
                alarm5man()
                alarm6woman()
                sentinal()
                
#alarm call false - listen
def alarmlisten2():
                print("Listen to subject false alarm")
                ledalarm.off()
                alarmwomanlisten2()
                sentinal()
                
#make choice when false alarm is called
def alarmfalse():
        while True:
                call = GPIO.input(26)
                listen = GPIO.input(19)
                stop = GPIO.input(13)
                if call == False:
                        print('Call')
                        alarmcall2()
                elif listen == False:
                        print("Listen")
                        alarmlisten2()
                elif stop == False:
                        print("Stop")
                        sentinal()
                        
#MOVE DEFINITIONS TRUE
#Define all thje audio functions needed to run the move alarm - True
def move1man():
        song = "./Music/6.mp3"
        print("Ik kreeg net een melding, ben je gevallen?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/6.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def move1woman():
        song = "./Music/31.wav"
        print("Ja, ik heb mijn been pijn gedaan!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/31.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def move2man():
        song = "./Music/7.mp3"
        print("Ik bel om hulp en kom er nu aan")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/7.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def movewomanlisten1():
        song = "./Music/36.wav"
        print("*stilte*")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/36.wav")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
#Move alarm true - call
def movecall1():
                print("Call subject move true")
                ledmove.off()
                callsound()
                move1man()
                move1woman()
                move2man()
                sentinal()
                
#Move alarm true - listen
def movelisten1():
                print("Listen to subject move true")
                ledmove.off()
                movewomanlisten1()
                sentinal()
                
#Make choice when true move alarm is called
def movetrue():
        while True:
                call = GPIO.input(26)
                listen = GPIO.input(19)
                stop = GPIO.input(13)
                if call == False:
                        print('Call')
                        movecall1()
                elif listen == False:
                        print("Listen")
                        movelisten1()
                elif stop == False:
                        print("Stop")
                        sentinal()

#MOVE DEFINITIONS FALSE
#Define all thje audio functions needed to run the move alarm - False
def move2woman():
        song = "./Music/32.wav"
        print("*geluid serie met gelach op de achtergrond")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/32.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                        
def move3man():
        song = "./Music/8.mp3"
        print("Ik kreeg net een melding, ben je gevallen?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/8.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def move3woman():
        song = "./Music/20.wav"
        print("Oh nee, ik denk een vals alarm, alles gaat goed hier!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/20.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def move4man():
        song = "./Music/10.mp3"
        print("Prima, ik ben over ongeveer een uurtje thuis!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/10.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
def move4woman():
        song = "./Music/21.wav"
        print("Tot zo!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/21.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def movewomanlisten2():
        song = "./Music/33.wav"
        print("*Serie met gelach op de achtergrond*")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/33.wav")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
#Move alarm false - call
def movecall2():
                print("Call subject move false")
                ledmove.off()
                callsound()
                move2woman()
                move3man()
                move3woman()
                move4man()
                move4woman()
                sentinal()
                
#Move alarm false - listen
def movelisten2():
                print("Listen to subject move false")
                ledmove.off()
                movewomanlisten2()
                sentinal()
                
#Make choice when false move alarm is called
def movefalse():
        while True:
                call = GPIO.input(26)
                listen = GPIO.input(19)
                stop = GPIO.input(13)
                if call == False:
                        print('Call')
                        movecall2()
                elif listen == False:
                        print("Listen")
                        movelisten2()
                elif stop == False:
                        print("Stop")
                        sentinal()

#SOCIAL DEFINITIONS
#Define all thje audio functions needed to run the social notification
def social1man():
        song = "./Music/11.mp3"
        print("Hey, gaat alles goed daar?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/11.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def social1woman():
        song = "./Music/22.wav"
        print("Jawel, alles gaat zijn gangetje")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/22.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def social2man():
        song = "./Music/12.mp3"
        print("Zal ik vanmiddag even langs komen voor een bakje koffie?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/12.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def social2woman():
        song = "./Music/23.wav"
        print("Oh, dat lijkt me echt heel erg gezellig!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/23.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def social3man():
        song = "./Music/13.mp3"
        print("Dan kom ik om 3 uur even langs!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/13.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def social3woman():
        song = "./Music/24.wav"
        print("Tot zo!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/24.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def socialwomanlisten():
        song = "./Music/35.wav"
        print("gerommel op de achtergrond")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/35.wav")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
#Social notification - call
def socialcall():
                print("Call subject social")
                ledsocial.off()
                callsound()
                social1man()
                social1woman()
                social2man()
                social2woman()
                social3man()
                social3woman()
                sentinal()
                
#Social notification - listen
def sociallisten():
                print("Listen to subject social")
                ledsocial.off()
                socialwomanlisten()
                sentinal()
                
#Make choice when social notification called
def socialchoice():
        while True:
                call = GPIO.input(26)
                listen = GPIO.input(19)
                stop = GPIO.input(13)
                if call == False:
                        print('Call')
                        socialcall()
                elif listen == False:
                        print("Listen")
                        sociallisten()
                elif stop == False:
                        print("Stop")
                        sentinal()

#ROAMING DEFINITIONS
#Define all the audio functions needed to run the roaming notification
def roamingman():
        song = "./Music/14.mp3"
        print("Hallo? Is daar iemand?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/14.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def roamingwoman():
        song = "./Music/36.wav"
        print("*Stilte*")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/36.wav")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
#Roaming notification - call
def roamingcall():
                print("Call subject roaming")
                ledwander.off()
                callsound()
                roamingman()
                roamingwoman()
                sentinal()
                
#Roaming notification - listen
def roaminglisten():
                print("Listen to subject roaming")
                ledwander.off()
                roamingwoman()
                sentinal()
                
#Make choice when roaming notification called
def roamingchoice():
        while True:
                call = GPIO.input(26)
                listen = GPIO.input(19)
                stop = GPIO.input(13)
                if call == False:
                        print('Call')
                        roamingcall()
                elif listen == False:
                        print("Listen")
                        roaminglisten()
                elif stop == False:
                        print("Stop")
                        sentinal()                        

#EATING DEFINITIONS
#Define all thje audio functions needed to run the eating notification
def eating1man():
        song = "./Music/15.mp3"
        print("Zorg je wel dat je voldoende eet?")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/15.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def eating1woman():
        song = "./Music/25.wav"
        print("Ik heb niet zo veel zin in eten de afgelopen dagen")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/25.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def eating2man():
        song = "./Music/16.mp3"
        print("Heb je anders zin in pannenkoeken? Daar houd je van toch? Dan kom ik ze straks even maken")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/16.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def eating2woman():
        song = "./Music/26.wav"
        print("Is goed!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/26.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def eating3man():
        song = "./Music/17.mp3"
        print("Tot vanavond!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/17.mp3")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def eating3woman():
        song = "./Music/27.wav"
        print("Tot vanavond!")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/27.wav")
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
def eatingwomanlisten():
        song = "./Music/35.wav"
        print("*Gerommel op de achtergrond*")
        pygame.init()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load("./Music/35.wav")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
#Eating notification - call
def eatingcall():
                print("Call subject eating")
                ledeat.off()
                callsound()
                eating1man()
                eating1woman()
                eating2man()
                eating2woman()
                eating3man()
                eating3woman()
                sentinal()
                
#Eating notification - listen
def eatinglisten():
                print("Listen to subject eating")
                ledeat.off()
                eatingwomanlisten()
                sentinal()
                
#Make choice when eating notification called
def eatingchoice():
        while True:
                call = GPIO.input(26)
                listen = GPIO.input(19)
                stop = GPIO.input(13)
                if call == False:
                        print('Call')
                        eatingcall()
                elif listen == False:
                        print("Listen")
                        eatinglisten()
                elif stop == False:
                        print("Stop")
                        sentinal()

#MAIN PROGRAM WHERE SUBJECT DATA IS SEND TO 
def sentinal():
        while True:
                print("start program")
                ledalarm.off()
                ledmove.off()
                ledsocial.off()
                ledwander.off()
                ledeat.off()
                try:
                        data = conn.recv(BUFFER_SIZE) #Receive maximum of BUFFER_SIZE characters in data
                        if len(data) == 0:
                                break;
                except socket.error:
                        break;
                print "received data:", data
                if data=="Huilen!":
                        ledalarm.on()
                        alarmtrue()
                elif data=="Oops!":
                        print("Gevallen")
                        ledmove.on()
                        movetrue()
                elif data=="Alleen!":
                        print("social")
                        ledsocial.on()
                        socialchoice()
                elif data=="Dwalen!":
                        print("roaming")
                        ledwander.on()
                        roamingchoice()
                elif data=="Eten!":
                        print("eten")
                        ledeat.on()
                        eatingchoice()
                elif data=="Huilen!False":
                        print("Vals Huilen!")
                        ledalarm.on()
                        alarmfalse()
                elif data=="Oops!False":
                        print("Vals gevallen")
                        ledmove.on()
                        movefalse()
                elif data=="Stop!":
                        print("Stop!")
                        ledalarm.on()
                        ledmove.on()
                        ledsocial.on()
                        ledwander.on()
                        ledeat.on()
                        time.sleep(10)
                conn.send(data)  # echo
        
def my_callback(channel):
        print("stop button has been pressed")
        start = False
        s.recv(1024)

GPIO.add_event_detect(13, GPIO.FALLING, callback=my_callback, bouncetime=300)
                
#Catch CTRL + C
conn = False	
s = False

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT)) #Create the server socket
        s.listen(1) # Start listening on serversocket for open connections
        conn, addr = s.accept() #Accept a single connection and do stuff with it
        print 'Connection address:', addr
        while True:
                print("1st thread started")
                if stop== True:
                        start = True
                while(start== True):
                        sentinal()
                	
except KeyboardInterrupt:
        print 'Closing server...'

         # Close connection if one exists
        if conn:
                conn.close()
         # Close listening server socket
        if s:
                s.close()
