from scapy.all import *
import sys
import time



class Scanner():



	def __init__(self,**kwargs):
		'''
		Initialize objects with destination and source addresses
		dest = <destination>, src = <source>
		'''

		try:
			self.source = kwargs['src']
			self.dest = kwargs['dest']
		except KeyError:
			print('Ensure you use the specified object initialization\nscanner = Scanner(src = <source>, dest = <destination>)')
			sys.exit()

	def ethernet(self):

		'''

		- Destination MAC adress
		- Source MAC adress
		- Tag :TPID, PRI, 
		- Length/Type
		- Data
		- FCS 

		'''

		eth = Ether(dst = self.dest, src = self.source)
		eth.show()
		pass

	def ip(self):
		'''
		  version   = 4 /6
		  ihl       = None
		  tos       = 0x0
		  len       = None
		  id        = 1
		  flags     = 
		  frag      = 0
		  ttl       = 64
		  proto     = hopopt
		  chksum    = None
		  src       = 127.0.0.1
		  dst       = 127.0.0.1
		'''

		ip = IP(dst=self.dest)
		ip.show()
		pass

	def icmp(self):

		pass
	def tcp(self):
		pass

	def arp(self):
		pass

	def arp():
		pass

	def send_receive():
		pass

	def send():
		pass




