from capture import sniff_packets
import os


def test_sniff_packets():
    iface_name = 'wlp0s20f3'
    filter_string = 'port 443'
    output_file = "test_capturepackets.pcap"

    number_of_captures = sniff_packets(iface_name, filter_string, output_file)

    assert number_of_captures > 0
    assert (iface_name,'Ethernet')
    assert (filter_string,'port 443')
    assert os.path.exists(output_file) == True
    
