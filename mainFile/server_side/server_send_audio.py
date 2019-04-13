### Server
import socket
from threading import *
import socket
import pygame
import pygame.camera
from pygame.locals import *
import subprocess


def server():
    ("\nServer started at " + str(socket.gethostbyname(socket.gethostname())) + " at port " + str(5005))  
    port = 5006
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("192.168.4.1",port))
    serversocket.listen(1)
     
    while(True):
        connection, address = serversocket.accept()
#        connection.close()
        subprocess.call("arecord /home/pi/Desktop/a.wav -D sysdefault:CARD=1 --duration=1", shell=True)
#        connection, address = serversocket.accept()
        with open("/home/pi/Desktop/a.wav", "rb") as f:
            for l in f:
                connection.sendall(l)
        connection.close()
        
        print("audio sent")
server()