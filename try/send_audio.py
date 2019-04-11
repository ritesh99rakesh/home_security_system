### Server
import socket
import socket
import pygame
import pyaudio
import subprocess


def server():     
    while(True):
        clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(("192.168.4.1", 5007))
        subprocess.call("arecord a.wav --duration=3", shell=True)

        with open("a.wav", "rb") as f:
            for l in f:
                clientsocket.sendall(l)
        clientsocket.close()
        
        print("audio sent")
server()