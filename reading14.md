Ops301d2 - Reading 14

https://www.varonis.com/blog/port-scanning-techniques/ 

“There are two kinds of network ports on each computer (65,536 of each for a total of 131,082 network ports):
TCP and UDP”
Well-known ports 1-1023
“TCP ports 1024 – 49151 are available for use by services or applications, and you can register them with IANA, so they are considered semi-reserved. Ports 49152 and higher are free to use.”
“A port scanner sends a TCP or UDP network packet and asks the port about their current status. The three types of responses are below:
Open, Accepted: The computer responds and asks if there is anything it can do for you.
Closed, Not Listening: The computer responds that “This port is currently in use and unavailable at this time.”
Filtered, Dropped, Blocked: The computer doesn’t even bother to respond.”
Part of the cyber kill chain
Using nmap, port scanning can be done on a variety of levels.
Ping Scanner
Simplest of port scans. “Ping scans aren’t technically port scanning techniques, as the best you can get back is that there is a computer on the other end, but it’s related and usually the first task before you do a port scan.”
TCP Half Open
the TCP half-open port scan, sometimes referred to as an SYN scan “a fast and sneaky scan that tries to find potential open ports on the target computer.”
“SYN packets request a response from a computer, and an ACK packet is a response. In a typical TCP transaction, there is an  SYN, an ACK from the service, and a third ACK confirming message received.”
 hard to detect because it never completes the full TCP 3 way-handshake. “The scanner sends an SYN message and just notes the SYN-ACK responses. The scanner doesn’t complete the connection by sending the final ACK: it leaves the target hanging.”
“Any SYN-ACK responses are possibly open ports. An RST(reset) response means the port is closed, but there is a live computer here. No responses indicate SYN is filtered on the network. An ICMP (or ping) no response also counts as a filtered response.
TCP half-open scans are the default scan in NMAP.”
TCP Connect
“basically the same as the TCP Half-Open scan, but instead of leaving the target hanging, the port scanner completes the TCP connection.”
intrusion detection systems (IDS)  on the target sees the completion, hence not likely to be used maliciously
UDP
UDP scans are slower than TCP scans, Defend UDP ports the same as TCP ports.
“UDP scans work best when you send a specific payload to the target.
One more logical use of a UDP scan is to send a DNS request to UDP port 53 and see if you get a DNS reply. If you do get a response, you know that there is a DNS server on that computer. A UDP scan can be useful to scout for active services that way, and the Nmap port scanner is preconfigured to send requests for many standard services.”
Difference Between TCP and UDP
“TCP and UDP are the two most common protocols in use for Internet Protocol (IP) networks. Transmission Control Protocol (TCP) is a nice orderly transaction protocol: TCP sends each packet in order, complete with error checking, verification, and a 3-way handshake to confirm each packet is successful.
UDP doesn’t have any error checking but tends to be faster. Live streaming and online video games often use UDP for this reason. UDP is a connectionless protocol, so programs that use UDP just send the data – and if you miss a packet, you will never get it again.”
Stealth Scanning
port scans  detection 
When you send a port scan with a packet and the FIN flag, you send the packet and not expecting a response. If you do get an RST, you can assume that the port is closed. If you get nothing back, that indicates the port is open. Firewalls are looking for SYN packets, so FIN packets slip through 
Additional Scanning Techniques
TCP ACK scan: to map firewall rulesets
TCP Window scan: can differentiate open ports from closed ports but only works on a minority of systems
–scanflags: for the advanced user that wants to send their custom TCP flags in a scan, you can do that in Nmap
How to Detect a Port Scan?
“One is a dedicated port scan detector software application, like PortSentry or Scanlogd.
Netcat includes port scanning functionality as well as the ability to create a simple chat server or program different packets for testing purposes.
Intrusion detection systems (IDS) are another way to detect port scans. Look for an IDS that uses a wide variety of rules to detect the various kinds of port scans that aren’t merely threshold-based.”
Why Should You Run a Port Scan?
You should run port scans proactively to detect and close all possible vulnerabilities that attackers might exploit.
good habit schedule. review and audit all open ports to verify they are being used correctly and that any applications that do use open ports are secure and protected from known vulnerabilities.
Implications of Running a Port Scan
services or computers might fail from a port scan. “This is for internal systems more so than internet-facing systems, but it can happen.”
“Port scans are a critical part of building a good defense from cyberattacks. Attackers are using port scans, as well. You need to beat them to the punch and close down possible attack vectors and make their lives as difficult as possible.”
