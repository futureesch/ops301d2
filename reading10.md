Ops301d2 - reading 11

https://www.geeksforgeeks.org/network-address-translation-nat/ 

Network address translation (NAT) converts local IP network addresses into WAN, public-facing ip addresses. 

Inside and Outside are used to refer to both LAN and WAN of a primary network and let’s say, a secondary, hence “outside” network. 

NAT Types
Static - Typically used for 1:1 web-hosting 
Dynamic - Unregistered ips so long as the pool is free; otherwise the packets will be dropped
Port - Shoe-horning an ip with multiple hosts by using the ports to distinguish traffic; a good cost-effective solution

“Advantages of NAT –

NAT conserves legally registered IP addresses .
It provides privacy as the device IP address, sending and receiving the traffic, will be hidden.
Eliminates address renumbering when a network evolves.

Disadvantage of NAT –

Translation results in switching path delays.
Certain applications will not function while NAT is enabled.
Complicates tunneling protocols such as IPsec.
Also, router being a network layer device, should not tamper with port numbers(transport layer) but it has to do so because of NAT.”
