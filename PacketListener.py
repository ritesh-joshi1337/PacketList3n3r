import scapy.all as scapy
from scapy_http import http

def packetlistener(interface):

    scapy.sniff(iface=interface,store=False,prn=packet_analyse)
#we wont be storing it for now, jsut display the contents of traffic of the ethernet network
def packet_analyse(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

packetlistener("eth0")
