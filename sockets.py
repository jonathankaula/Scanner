import socket




class TcpSocketServer:

	def __init__(self,address,port):
		self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.address = address
		self.port = port
		

	def connect(self):
		self.tcp_socket.connect((self.address,self.port))

class TCPServer(TcpSocketServer):

	def p():
		pass

class TCPClient(TcpSocketServer):

	def p():
		pass


class UDPServer:

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

		while(1):
			message, address = udp_socket.recvfrom(self.buf_size)
			print(f"CLient Message: {message}\nClient IP: {address}")

			self.send(message.upper(),udp_socket)


	def send(self,msg,udp_socket):
		'''
		Send Messages
		'''
		message = str.encode(msg)
		udp_socket.sendto(message,self.ip)



class UDPclient(UDPServer):

	def __init__(self):
		self.client_port = 3455


	def udp_client():
		udp_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		msg = 'jonathan is a good boy'
		message = str.encode(msg)
		send(message,udp_socket)

		message, address = udp_socket.recvfrom(self.buf_size)
		print(f"Server Message: {message}\nServer IP: {address}")


udpserver = UDPServer()
udpserver.udp_server()






