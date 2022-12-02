# NetForensia


This python script automatically generates:
   
   
   1.pcap file -which sniffs the packet and (Cyber attack performed)-------
   
   
   2.Snort rules applied on .pcap file which generates (forensics performed)
    a. pcap file generated
    b. .pcap file the correct packet number to display the packet
    c.generate snort rules from this packet which indicates the malicious packets
    
    a.Requirements

    1.Python 
    2.scapy
    3.pyshark
    4.wireshark
    
    b.Implementation  
    
    1.Option -c will automatically capture the packets using wireshark and saves it in capturpackets.pcap file.

    =>python snortfile.py -c <interface_name>

   2.The script shows the summary of the pcap file. Just use -r option.
      
    =>python snortfile.py -r capturepackets.pcap
  
   3.Use of -p option with the correct packet number to display the specified packet.

   => python snortfile.py -r capturepackets.pcap -p 2
  
   4.Use the -s option to generate snort rules from this packet.
   
    => python snortfile.py -r packets.pcap -p 1 -s
   

    
    
