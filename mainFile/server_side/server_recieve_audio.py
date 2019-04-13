#### Server
#import socket
#from threading import *
#import socket
#import pygame
#import pygame.camera
#from pygame.locals import *
#import pyaudio
#import subprocess
#
#
#def server():
#    ("\nServer started at " + str(socket.gethostbyname(socket.gethostname())) + " at port " + str(5005))  
#    port = 5006
#    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    serversocket.bind(("192.168.4.1",port))
#    serversocket.listen(1)
#     
#    while(True):
#        connection, address = serversocket.accept()
##        connection.close()
#        subprocess.call("arecord /home/pi/Desktop/a.wav -D sysdefault:CARD=1 --duration=3", shell=True)
##        connection, address = serversocket.accept()
#        with open("/home/pi/Desktop/a.wav", "rb") as f:
#            for l in f:
#                connection.sendall(l)
#        connection.close()
#        
#        print("audio sent")
#server()
#

#!usr/bin/env python  
#coding=utf-8

import socket
import time
import subprocess


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.4.1", 5007))
server_socket.listen(1)

while True:
    client_socket, address = server_socket.accept()
    with open('audio_file_processing.wav', 'wb') as f:
        while True:
            received_audio = client_socket.recv(1024)
            if not received_audio:
                print('error in audio')
                break
            f.write(received_audio)
    print('audio received')
    with open('audio_file_processing.wav', 'rb') as f:
        with open('audio_file.wav', 'wb') as f1:
            for line in f:
                f1.write(line)  
    subprocess.call("aplay audio_file.wav", shell=True)




















#
















