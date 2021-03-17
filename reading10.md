Ops301d2 - reading 10

Virtual Private Networks mask the public facing IP address of a given network. This can obfuscate easy sniffing access attackers prefer. Users can obviate geolocked locations. Overall, individual networks can achieve a greater degree of security deploying VPNs.

Types of VPNs
Remote Access - 
temporary connection between two or more users and a central location. 
useful tool for companies with remote workers either on the road or in their homes. workers can access private or sensitive information on the company’s servers to get access to the job-related resources
Intranet-based Site-to-Site
connects more than one local-area network (LAN) to form a wide-area network (WAN). this kind of setup is used for software-defined WAN (SD-WAN). useful for combining resources from different areas--in a secure manner
helpful if each site either develops its own resources or houses unique processes that the entire company would benefit from having access to. 
Extranet-based Site-to-Site
often used by two or more different WANs/LANs that want to share certain resources but keep others private. each site connects to the VPN and chooses what they want to make available to the others 

Creating an Internet-based VPN
a VPN gateway secures the data traveling back and forth.

a tunnel connecting two networks, requires the following components:

A base network in one location
A satellite network in another location
A tunnel with security gateways on each end

“The tunnel “burrows through” or sits on top of a physical internet connection. However, the tunnel protects the traffic flowing through it from being accessed by people using the physical network.” 

set it up, with a gateway at each site. “The first gateway the data meets as it enters the tunnel will encrypt the data.” 

at its destination, the other gateway decrypts the data so the network on the other side can read it. 

“The gateway may incorporate a network access server and a secure access service edge (SASE), which requires the user to enter credentials before they gain access to the VPN.”

You can also use a firewall, 

Creating an MPLS Site-to-Site VPN

MPLS depends on infrastructure made available by the VPN provider, as opposed to the company that uses the VPN. configuration of MPLS VPN creates VPN connections between the primary and satellite sites.

works through labels that route data packets to destination, not IP addresses. Nodes interpret the labels and send the data packet to the next hop. This enables direct links between the nodes. MPLS site-to-site VPN, can route the data directly from A to B. 

“To create an MPLS site-to-site VPN, you first have to set up a broadband IP network, which will serve as the backbone for the MPLS network. The organization then has to equip each site with an MPLS-suitable switch that connects to a router. This allows the data that passes through the switch to be sent using MPLS. As a data packet at location A hits the switch, it gets encoded using MPLS. Then, it passes to location A’s router and straight to location B’s router and switch.”

Why Implement a Site-to-Site VPN

The number of locations
Business size
The distance between each location
The resources the locations have to share with each other

Components of VPN
Watertight Security - coupled with good SOPs
Ease of Operations - 
Simple and Secure Scalability
Business Continuity
Flexible Deployment
