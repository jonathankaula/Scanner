import socket
import time



class UDPserver:

	def __init__(self):

		self.ip = '127.0.0.1'
		self.port = 5000
		self.buf_size = 1024


	def udp_server(self):
		'''
		Create a datagram socket
		Bind to address and ip

		'''

		udp_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		udp_socket.bind((self.ip,self.port))
		print("UDP server up and listening")

		self.listen(udp_socket)



	def listen(self,udp_socket):
		'''
		Listen for incoming datagrams
		'''

		while(True):
			message, address = udp_socket.recvfrom(self.buf_size)
			t = time.localtime()

			self.send(message,udp_socket,address)


	def send(self,msg,udp_socket,address):
		'''
		Send Messages
		'''
		udp_socket.sendto(msg,address)