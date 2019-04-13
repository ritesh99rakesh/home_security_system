import socket
import time



# clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientsocket.connect(("192.168.4.1", 5006))

while True:
	clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(("192.168.4.1", 5006))
	with open('audio_file_processing.wav', 'wb') as f:
		while True:
			received_audio = clientsocket.recv(1024)
			if not received_audio:
				break
			f.write(received_audio)
	print('audio received')
	with open('audio_file_processing.wav', 'rb') as f:
		with open('audio_file.wav', 'wb') as f1:
			for line in f:
				f1.write(line)	
			
	# time.sleep(2)
