import socket
HOST='192.168.4.1'
PORT=5005
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    data=s.recv(1)
    print(data)
s.close()
