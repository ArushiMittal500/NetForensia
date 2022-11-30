import unittest
import os


class test(unittest.TestCase):
    def __init__(self,iface_name,filter_string,interface,bpf_filter):
        self.iface_name=iface_name
        self.filter_string=filter_string
        self.interface=interface
        self.bpf_filter=bpf_filter
        pass
         
    def capture(self,interface,bpf_filter,iface_name,filter_string):
        self.assertNotEqual(interface,'')
        self.assertNotEqual(bpf_filter,'')
        self.assertEqual(iface_name,'Ethernet')
        self.assertEqual(filter_string,'port 443')       
    def capturesniff(self,timeout,packet_count):
        self.assertNotEqual(timeout,0)
        self.assertCountEqual(packet_count,50)
    def generted(self,path):
        print(os.path.isfile(path))
  
