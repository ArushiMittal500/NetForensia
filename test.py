import unittest
import pyshark

class test(unittest.TestCase):
    def __init__(self,iface_name,filter_string,interface,bpf_filter):
        self.iface_name=iface_name
        self.filter_string=filter_string
        self.interface=interface
        self.bpf_filter=bpf_filter
        pass
    def test_iface_name(self,iface_name):
        self.assertEqual(iface_name,'Ethernet')
    def test_filter_string(self,filter_string):
        self.assertEqual(filter_string,'port 443')       
    def capture(self,interface,bpf_filter):
        self.assertNotEqual(interface,'')
        self.assertNotEqual(bpf_filter,'')       
    
    
    
    
    iface_name = 'Ethernet'
    filter_string = 'port 443'
    capture = pyshark.LiveCapture(
        interface=iface_name,
        bpf_filter=filter_string,
        output_file="packet.pcap")
    capture.sniff(timeout=5, packet_count=50)
    if len(capture) > 0:
        for packet in capture:
            print('source: ' + packet.ip.src + " Destination: " + packet.ip.dst)