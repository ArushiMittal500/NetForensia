import pyshark

def sniff_packets(iface_name, filter_string, output_file):
    capture = pyshark.LiveCapture(
        interface=iface_name,
        bpf_filter=filter_string,
        output_file=output_file
    )
    capture.sniff(timeout=5, packet_count=50)
    print(len(capture))
    if len(capture) > 0:
        for index, packet in enumerate(capture):
            if "ip" in packet:
                print(f'{index} source: {packet.ip.src} Destination:  {packet.ip.dst}')

    return len(capture)



if __name__ == "__main__":
    iface_name = 'wlp0s20f3'
    filter_string = 'port 443'
    output_file="capturepackets.pcap"
    sniff_packets(iface_name, filter_string, output_file)
