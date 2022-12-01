from scapy.all import Ether, ARP, srp, send
import argparse
import time
import os
import sys


def linux_iproute_enable():
	"""
	Enables IP route ( IP Forward ) in linux-based distro
	"""
	file_path = "/proc/sys/net/ipv4/ip_forward"
	with open(file_path) as f:
		if f.read() == 1:
			# already enabled
			return
	with open(file_path, "w") as f:
		print(1, file=f)


def enable_iproute(verbose=True):
	"""
	Enables IP forwarding in linux
	"""
	if verbose:
		print("[!] Enabling IP Routing...")
	linux_iproute_enable()
	if verbose:
		print("[!] IP Routing enabled.")


def get_mac(ip):
	"""
	Returns MAC address of any device connected to the network
	If ip is down, returns None instead
	"""
	ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), verbose=0)
	if ans:
		return ans[0][1].src



if __name__ == '__main__':
	#enable iprouting
	enable_iproute()

	#Get MAC of target ip
	Mac = get_mac('192.186.23.126')