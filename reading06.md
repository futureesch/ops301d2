Ops301d2 - reading06

https://www.comptia.org/blog/layers-2-and-3-osi-model 

Great review of the OSI model at-large, but a nice detailed look at what’s happening in layer 2 and 3. 

Layer 2

Divided by the Media Access Controller (MAC) address and Data link sub-layers. MAC addresses are unique and burnt into the host machine. So long as they reside in the same domain, this can be an effective way to communicate between workstations. The flow of network traffic is done through specific ports by switches that learn the addresses to send packets of information as a means of sending information using the network without burdening the network with congestion.

Data link sublayer came as the need to expand networks beyond flat-physical networks would produce congestion and latency issues. Protocols for handling data frames -- packets of info for both the send and the recipient

Layer 3

The networking layer structures data transmission for efficiency between networks. IP addressing elevates the delivery of data to the envelope of routers. There, the sender and recipient are identified with network, subnet, and host addressing to communicate between networks.

https://www.comptia.org/content/articles/what-is-wireshark-and-how-to-use-it 

Wireshark - Software application designed to allow sysadmins to analyze network activity more deeply to suss out issues and make better-informed network security decisions.

As a “packet-sniffer,” Wireshark does what you would expect:

“
Packet Capture: Wireshark listens to a network connection in real time and then grabs entire streams of traffic – quite possibly tens of thousands of packets at a time.
Filtering: Wireshark is capable of slicing and dicing all of this random live data using filters. By applying a filter, you can obtain just the information you need to see.
Visualization: Wireshark, like any good packet sniffer, allows you to dive right into the very middle of a network packet. It also allows you to visualize entire conversations and network streams.”
Fun spelunking analogy and exploratory relationship to what you could find using this tool.
It has a variety of uses to a number of IT professional situations.
Brush up on:
 “the three-way TCP handshake and various protocols, including TCP, UDP, DHCP and ICMP.”
Analyzer limited to traffic between your pc and the remote system it is talking to
Lacks Intrusion Detection System (IDS) notifications)
Cannot decrypt encrypted traffic.
Uses cases for what caused a network slow down and the ability to analyze router and switches for more efficient configuration
