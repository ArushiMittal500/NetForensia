import pyshark
iface_name = 'Ethernet'
filter_string = 'port 443'
capture = pyshark.LiveCapture(
    interface=iface_name,
    bpf_filter=filter_string,
    output_file="capturepackets.pcap"
)
capture.sniff(timeout=5, packet_count=50)
if len(capture) > 0:
    for packet in capture:
        print('source: ' + packet.ip.src + " Destination: " + packet.ip.dst)