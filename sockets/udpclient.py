import socket




class UDPclient():

	def __init__(self):
		self.ip = '127.0.0.1'
		self.buf_size = 1024


	def udp_client(self):
		'''
		Create a UDP socket
		Send message to server
		'''

		udp_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		msg = 'jonathan is a good boy'

		self.send(msg,udp_socket)

		message, address = udp_socket.recvfrom(self.buf_size)
		print(f"Server Message: {message}\nServer IP: {address}")


	def send(self,msg,udp_socket):
		'''
		Send Messages
		'''
		message = str.encode(msg)
		udp_socket.sendto(message,(self.ip,5000))
