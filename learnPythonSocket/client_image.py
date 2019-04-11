#!/usr/bin/python
# TCP client example
import socket,os
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.4.1", 5005))
k = ' '
size = 1024

while(1):
    print("Do you want to transfer a \n1.Text File\n2.Image\n3.Video\n")
    k = input()
    print(k.endcode('utf-8'))
    client_socket.send(k.encode('utf-8'))
    k = int (k)
    if(k == 1):
        print("Enter file name\n")
        strng = input()
        client_socket.send(strng.encode('utf-8'))
        size = client_socket.recv(1024)
        size = int(size)
        print("The file size is - ",size," bytes")
        size = size*2
        strng = client_socket.recv(size)
        print ("\nThe contents of that file - ")
        print (strng)

    if (k==2 or k==3):
        print ("Enter file name of the image with extentsion (example: filename.jpg,filename.png or if a video file then filename.mpg etc) - ")
        fname = input()
        client_socket.send(fname.encode('utf-8'))
        fname = 'documents/'+fname
        fp = open(fname,'wb')
        while True:
            strng = client_socket.recv(512)
            if not strng:
                break
            fp.write(strng)
        fp.close()
        print ("Data Received successfully")
        exit()
        #data = 'viewnior '+fname
        #os.system(data)
