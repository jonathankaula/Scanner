from scapy.all import *
import multiprocessing


class Scans:

	def __init__(self, dest,dport):

		self.dest = dest
		self.dport = dport

		pass

	

	def arp_ping(ip_range):
		ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=5)
		hosts = []
		for s, r in ans:
			hosts.append(r.psrc)
		return hosts

	def icmp_ping(ip_list):
		ans, unans = sr(IP(dst=ip_list)/ICMP(), timeout=3)
		packets = []
		for s, r in ans:
			packets.append((s, r))
		return packets


	def protocol_scan(ip_address):
		ans, unans = sr(IP(dst=ip_address,proto=(0,255))/"SCAPY",retry=2)
		packets = []
		for s, r in ans:
			packets.append((s, r))
		return packets

	def udp_scan(ip_address):
		ans, unans = sr(IP(dst=ip_address)/UDP(dport=(1,65535)), timeout=3)
		packets = []
		for s, r in ans:
			if r.haslayer(UDP):
				packets.append(r)
		return packets


	def ack_scan(ip_address):
    #Perform an ACK scan on the destination IP address and port specified in self.dest and self.dport
    ans, unans = sr(IP(dst=ip_address)/TCP(dport= (1,65535) ,flags="A"))

    #Initialize lists to store filtered and unfiltered ports
    unfiltered = []
    filtered = []

    #iterate through the sent packets and their corresponding responses
    for s,r in ans:
        if s[TCP].dport == r[TCP].sport:
            unfiltered.append(s[TCP].dport)
    return unfiltered


def christmas_scan(target_ip):
		open_ports = []
		unfiltered_ports = []
		filtered_ports = []

		# Send a TCP packet with the FIN, PSH, and URG flags set
		# This is known as a "Christmas scan" and is used to determine the state of a port
		for port in range(1, 65535):
			packet = IP(dst=target_ip)/TCP(dport=port, flags="FPU")
			response = sr1(packet, timeout=1, verbose=0)

			if response is None:
				unfiltered_ports.append(port)
			elif response.haslayer(TCP) and response[TCP].flags == 0x14:
				filtered_ports.append(port)
			elif response.haslayer(TCP) and response[TCP].flags == 0x12:
				open_ports.append(port)

		return open_ports, unfiltered_ports, filtered_ports


	def syn_scan(ip_address):
		#Perform a SYN scan on the IP range "192.168.1.0/24" on port 
		ans, unans = sr( IP(dst=ip_address)/TCP(dport=80,flags="S"))
		open_ports = []
		#iterate through the sent packets and their corresponding responses
		for s,r in ans:
			#check if the target host responded with a SYN-ACK packet
			if r[TCP].flags == 18:
				#if it did, add the destination port to the list of open ports
				open_ports.append(s[TCP].dport)
		#return the list of open ports
		return open_ports


ack = Scans('192.168.163.62',[80,480])
ack.ip_scan()

