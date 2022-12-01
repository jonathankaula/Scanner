import socket
import time



class UDPclient():

	def __init__(self):
		self.ip = socket.gethostbyname(socket.gethostname())
		self.buf_size = 1024


	def udp_client(self):
		'''
		Create a UDP socket
		Send message to server
		'''

		udp_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		
		rtt = []
		recv_pkt_count = 0
		for i in range(10):
			t = time.localtime()
			send_time = time.strftime("%H:%M:%S", t)
			s_time = time.time()
			print('ping %d %s' % (i+1,send_time))

			self.send('ping %d ' % (i+1),udp_socket)
			udp_socket.settimeout(5.0)

			try:
				message, address = udp_socket.recvfrom(self.buf_size)
				time.sleep(5)
				t = time.localtime()
				recv_time = time.strftime("%H:%M:%S", t)
				r_time = time.time()
				print('%s %s' % (message.decode(),recv_time),'\n')

				RTT = r_time - s_time
				rtt.append(RTT)
				recv_pkt_count+=1



			except socket.timeout:
				print('Request timed out\n')
				continue

		max_rtt = max(rtt)
		min_rtt = min(rtt)
		avg_rtt = (sum(rtt) / len(rtt))
		pkt_loss = (1-(recv_pkt_count/10))*100

		print(f'MAX RTT: {max_rtt}\nMIN RTT: {min_rtt}\nAVERAGE RTT: {avg_rtt}')
		print(f'PACKET LOSS: {pkt_loss}%')
		udp_socket.close()


	def send(self,msg,udp_socket):
		'''
		Send Messages
		'''
		message = str.encode(msg)
		udp_socket.sendto(message,(self.ip,5000))
