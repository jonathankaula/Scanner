# Server.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('127.0.0.1', 5000))
while True:
	# Generate random number in the range of 0 to 9. Both 0 and 9 are included.
	rand = random.randint(0, 9)
	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	# Capitalize the message from the client
	message = message.decode().upper()
	# If rand is less than 3, we consider the packet lost and do not respond
	if rand < 3:
		continue
	# Otherwise, the server responds
	serverSocket.sendto(message.encode(), address)