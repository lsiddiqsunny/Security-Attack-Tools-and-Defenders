# code from: https://pastebin.com/YCR3vp9B
#! /usr/bin/python
from logging import getLogger, ERROR # Import Logging Things
getLogger("scapy.runtime").setLevel(ERROR) # Get Rid if IPv6 Warning
from scapy.all import * # The One and Only Scapy
import sys 
from datetime import datetime # Other stuff
from time import strftime

try:
	target = input("[*] Enter Target IP Address: ") # Get Target Address
	min_port = input("[*] Enter Minumum Port Number: ") # Get Min. Port Num.
	max_port = input("[*] Enter Maximum Port Number: ") # Get Max. Port Num.
	try:
		if int(min_port) >= 0 and int(max_port) >= 0 and int(max_port) >= int(min_port): # Test for valid range of ports
			pass
		else: # If range didn't raise error, but didn't meet criteria
			print ("\n[!] Invalid Range of Ports")
			print ("[!] Exiting...")
			sys.exit(1)
	except Exception: # If input range raises an error
		print ("\n[!] Invalid Range of Ports")
		print ("[!] Exiting...")
		sys.exit(1)		
except KeyboardInterrupt: # In case the user wants to quit
	print ("\n[*] User Requested Shutdown...")
	print ("[*] Exiting...")
	sys.exit(1)

ports = range(int(min_port), int(max_port)+1) # Build range from given port numbers
start_clock = datetime.now() # Start clock for scan time
SYNACK = 0x12 # Set flag values for later reference
RSTACK = 0x14

def checkhost(ip): # Function to check if target is up
	conf.verb = 0 # Hide output
	try:
		ping = sr1(IP(dst = ip)/ICMP()) # Ping the target
		print ("\n[*] Target is Up, Beginning Scan...")
	except Exception: # If ping fails
		print ("\n[!] Couldn't Resolve Target")
		print ("[!] Exiting...")
		sys.exit(1)

def scanport(port): # Function to scan a given port
	try:
		srcport = RandShort() # Generate Port Number
		conf.verb = 0 # Hide output
		SYNACKpkt = sr1(IP(dst = target)/TCP(sport = srcport, dport = port, flags = "S")) # Send SYN and recieve RST-ACK or SYN-ACK
		pktflags = SYNACKpkt.getlayer(TCP).flags # Extract flags of recived packet
		if pktflags == SYNACK: # Cross reference Flags
			return True # If open, return true
		else:
			return False # If closed, return false
		RSTpkt = IP(dst = target)/TCP(sport = srcport, dport = port, flags = "R") # Construct RST packet
		send(RSTpkt) # Send RST packet
	except KeyboardInterrupt: # In case the user needs to quit
		RSTpkt = IP(dst = target)/TCP(sport = srcport, dport = port, flags = "R") # Built RST packet
		send(RSTpkt) # Send RST packet to whatever port is currently being scanned
		print ("\n[*] User Requested Shutdown...")
		print ("[*] Exiting...")
		sys.exit(1)

checkhost(target) # Run checkhost() function from earlier
print ("[*] Scanning Started at " + strftime("%H:%M:%S") + "!\n") # Confirm scan start

for port in ports: # Iterate through range of ports
	status = scanport(port) # Feed each port into scanning function
	if status == True: # Test result 
		print ("Port " + str(port) + ": Open") # Print status

stop_clock = datetime.now() # Stop clock for scan time
total_time = stop_clock - start_clock # Calculate scan time
print ("\n[*] Scanning Finished!") # Confirm scan stop
print ("[*] Total Scan Duration: " + str(total_time)) # Print scan time