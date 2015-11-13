
from scapy.all import *

if len(sys.argv) != 7:
	print 'arguments wrong'
	sys.exit(1)
import sys


conf.iface = sys.argv[1]
bssid = sys.argv[2]
target = sys.argv[3]
count = sys.argv[4]

conf.verb = 0


recs=rdpcap("/tmp/cap.pcap")
lrecs=len(recs)
pkts=[]
start=int(sys.argv[5])-1
end=int(sys.argv[6])-1

if (end >=lrecs):
    print "End value greater than number of pcap records"
    sys.exit()

x=start
while (x<=end):
    if(x==336):
        pkts.append(recs[x])
    x=x+1

#wireshark(outrecs)

for n in range(int(count)):
    for pkt in pkts:
        #pkt[Dot11].src ="68:D9:3C:54:7B:F8"
        pkt[Dot11].src =target
        #pkt[Dot11].dst = "A0:14:3D:69:B0:76"
        pkt[Dot11].dst=bssid
        sendp(pkt)
