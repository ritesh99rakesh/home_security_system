### Server
import socket
from threading import *
import socket
import pygame
import pygame.camera
from pygame.locals import *
import pyaudio


def server():
    ("\nServer started at " + str(socket.gethostbyname(socket.gethostname())) + " at port " + str(5005))  
    port = 5005
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("192.168.4.1",port))
    serversocket.listen(1)
    pygame.camera.init()
    print("init done")
    cam = pygame.camera.Camera("/dev/video0",(640,480),"RGB")
    cam.start()
    print("cam started")
    img = pygame.Surface((640,480))
    
    while True:
        connection, address = serversocket.accept()
        print("GOT_CONNECTION")
        cam.get_image(img)
        data = pygame.image.tostring(img,"RGB")
        connection.sendall(data)
        connection.close()


#def server():
#    try:
#        print("\nServer started at " + str(socket.gethostbyname(socket.gethostname())) + " at port " + str(5005))  
#        port = 5005
#        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        serversocket.bind(("192.168.4.1",port))
#        serversocket.listen(1)
#        pygame.camera.init()
#        print("init done")
#        cam = pygame.camera.Camera("/dev/video0",(640,480),"RGB")
#        cam.start()
#        print("cam started")
#        img = pygame.Surface((640,480))
#        while True:
#            connection, address = serversocket.accept()
#            print("GOT_CONNECTION")
#            cam.get_image(img)
#            data = pygame.image.tostring(img,"RGB")
#            connection.sendall(data)
#            connection.close()
#    except:
#        print('exited camera')
#        pass

server()



#
#import socket
#
#(HOST,PORT)=('localhost',19123)
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((HOST,PORT))
#
#with open('input', 'rb') as f:
#  for l in f: s.sendall(l)
#s.close()