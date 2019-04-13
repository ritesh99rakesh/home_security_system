from kivy.config import Config
Config.set('graphics','resizable',0)

import time

from kivy.core.window import Window
from kivy.core.audio import SoundLoader
Window.size = (600, 500)



from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import socket
from threading import *
from kivy.uix.image import Image
from kivy.cache import Cache
import pygame
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kv = '''
main:
	BoxLayout:
		orientation: 'vertical'
		padding: root.width * 0.05, root.height * .05
		spacing: '5dp'
		BoxLayout:
			size_hint: [1,.85]
			Image:
				id: image_source
				source: 'foo.jpg'
		BoxLayout:
			size_hint: [1,.15]
			GridLayout:
				cols: 5
				spacing: '10dp'
				Button:
					text: 'Close'
					bold: True
					on_press: root.close()
				Button:
					id: status
					text:'Play'
					bold: True
					on_press: root.playPause()
				Button:
					id: sound
					text: 'Listen'
					bold: True
					on_press: root.soundPlayPause()
				Button:
					id: door
					text: 'Open Door'
					bold: True
					on_press: root.openDoor()
				Button:
					text: 'Setting'
					bold: True
					on_press: root.setting()

'''
class main(BoxLayout):
	ipAddress = "192.168.4.1"
	port = 5005

	def playPause(self):
		if self.ipAddress == None or self.port == None:
			box = GridLayout(cols=1)
			box.add_widget(Label(text="Ip or Port Not Set"))
			btn = Button(text="OK")
			btn.bind(on_press=self.closePopup)
			box.add_widget(btn)
			self.popup1 = Popup(title='Error',content=box,size_hint=(.8,.3))
			self.popup1.open()
		else:
			if self.ids.status.text == "Stop":self.stop()
			else:
				self.ids.status.text = "Stop"
				Clock.schedule_interval(self.recv, 0.05)

	def soundPlayPause(self):
		if self.ids.sound.text == "Mute": self.mute_audio()
		else:
			self.ids.sound.text = "Mute"
			Clock.schedule_interval(self.audio, 1)

	def mute_audio(self):
		self.ids.sound.text = "Listen"
		Clock.unschedule(self.audio)

	def openDoor(self):
		if self.ids.door.text == "Close Door": self.close_door()
		else:
			self.ids.door.text = "Close Door"
			self.open_door()

	def close_door(self):
		self.ids.door.text = "Open Door"
		clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect(("192.168.4.1", 5008))
		clientsocket.send("1".encode('utf-8'))
		clientsocket.close()
		print("door closed")

	def open_door(self):
		clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect(("192.168.4.1", 5008))
		clientsocket.send("0".encode('utf-8'))
		clientsocket.close()
		print("door opened")


	def closePopup(self,btn):
		self.popup1.dismiss()

	def stop(self):
		self.ids.status.text = "Play"
		Clock.unschedule(self.recv)


	def audio(self, dt):
		sound = SoundLoader.load('audio_file.wav')
		if sound:
			sound.play()



	def recv(self, dt):
		clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect((self.ipAddress, self.port))
		received_video = []
		while True:
			recvd_data = clientsocket.recv(230400)
			if not recvd_data:
				print('video finished')
				break
			else:
				received_video.append(recvd_data)
		dataset_video = b''.join(received_video)
		print('type:', type(dataset_video))
		print('dataset size:', len(dataset_video))
		image = pygame.image.fromstring(dataset_video, (640, 480), "RGB") # convert received image from string
		pygame.image.save(image, "foo.jpg")
		print('image saved')
		self.ids.image_source.reload()
		print('image received')


	def close(self):
		App.get_running_app().stop()

	def setting(self):
		box = GridLayout(cols = 2)
		box.add_widget(Label(text="IpAddress: ", bold = True))
		self.st = TextInput(id= "serverText")
		box.add_widget(self.st)
		box.add_widget(Label(text="Port: ", bold = True))
		self.pt = TextInput(id= "portText")
		box.add_widget(self.pt)
		btn = Button(text="Set", bold=True)
		btn.bind(on_press=self.settingProcess)
		box.add_widget(btn)
		self.popup = Popup(title='Settings',content=box,size_hint=(.6,.4))
		self.popup.open()

	def settingProcess(self, btn):
		try:
			self.ipAddress = self.st.text
			self.port = int(self.pt.text)
		except:
			pass
		self.popup.dismiss()


class videoStreamApp(App):
	def build(self):
		return Builder.load_string(kv)

videoStreamApp().run()