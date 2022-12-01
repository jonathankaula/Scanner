from scapy.all import *
import multiprocessing


class Scans:

	def __init__(self, dest,dport):

		self.dest = dest
		self.dport = dport

		pass

	def arp_ping():
		ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24, timeout=2"))

	def ip_scan():
		ans, unans = sr(IP(dst="192.168.163.62",proto=(0,255))/"SCAPY",retry=2)

		for s,r in ans:
			s.show()
			r.show()

	def icmp_ping():
		ans, unans = sr(IP(dst="192.168.1.0/24")/ICMP(), timeout=3)

	def udp_ping():
		ans, unans = sr( IP(dst="192.168.*.1-10")/UDP(dport=0) )


	def dns_requests():
		ans = sr1(IP(dst="8.8.8.8")/UDP(sport=RandShort(), dport=53)/DNS(rd=1,qd=DNSQR(qname="secdev.org",qtype="A")))
		ans.an.rdata

	def ack_scan(self):
		
		ans, unans = sr(IP(dst=self.dest)/TCP(dport= self.dport ,flags="A"))
		unfiltered = []
		filtered = []
		for s,r in ans:
			if s[TCP].dport == r[TCP].sport:
				unfiltered.append(s[TCP].dport)

		for s in unans:
			filtered.append(s[TCP].dport)

		print(f'Unfiltered: {unfiltered}')
		print(f'filtered: {filtered}')


	def xmas_scan(self):
		ans, unans = sr(IP(dst=self.dest)/TCP(dport= self.dport ,flags="FPU"))
		for s,r in ans:
			r.show()

	def syn_scan():
		ans, unans = sr( IP(dst="192.168.1.0/24")/TCP(dport=80,flags="S") )

ack = Scans('192.168.163.62',[80,480])
ack.ip_scan()

