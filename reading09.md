ops301d2 - reading09

https://medium.com/@acropoiesis/cidr-block-notation-explained-in-2-minutes-1010ec0dbc15 

“When you create a network, the aim is to make sure there are enough available IP addresses for your use case, without making the CIDR block too large and wasteful.”

“The final digit after the “/” represents how many bits make up the mask.”

The larger the mask, the smaller the range. For example:
10.0.0.0/16
/16 is the available bits out of 32.
The range would be 10.0.0.0 - 10.0.255.255
Each spot is an octet, and with 16, that masks the right two octets
10.0.0./24
The range would be 10.0.0.0 - 10.0.0.255

https://www.subnet-calculator.com/cidr.php is really cool

https://www.comptia.org/blog/security-awareness-training-network-segmentation 

Network segmentation is a great way to deter malicious actors seeking easy opportunity targets. Additionally, by segmenting the network, privileged access can be limited, widespread attacks on the network as a whole can be thwarted, and boost performance by balancing usage.

The concept here is to frustrate the attacker so as to leave your network completely. This breakout is too good to paraphrase: 

Users: Users are a network in and of themselves. Make sure you have correct access control on your users in your active directory. Who needs the least privilege on your network? Privilege levels should be based on the user’s role in switching administration. How many admins have full access rights? Make sure you have less than a handful. Access control lists are typically already a part of your active directory server. The idea here is you are extending that practice to more components of your network.
Screened Subnet: This includes the subnetworks that expose externally facing systems – where the handshakes take place on your network. For example, it may include public-facing websites or other resources accessible via the internet. You want to separate things that the public can access from your local area network (LAN) and internal data that needs to be protected.
Guest Network: Guest Wi-Fi should be separate from the corporate Wi-Fi. This may seem like a no brainer, but I find a lot of smaller businesses never bother to set it up. Even residential routers include this feature – you can easily set up a guest Wi-Fi in your home!
IT Workstations: This is the dev network zone for IT. It’s where your IT staff does non-administrative work, and it should be segmented for testing. I would also recommend giving IT a dedicated internet circuit for testing. This can be a best effort, cheaper connection. Don’t let anyone else in the company have network access to it aside from IT.
Servers by Department: Do department servers need to talk to one another? Create a public drive and a private drive, and then segment access on the private drives to those within each team or department. This can limit the crawl of malware.
VoIP/Communications: Placing communications systems on their own network zone boosts performance and enhances quality. But in terms of network security, as communications move toward more APIs unique to your most used software as a service (SaaS) platforms, this network will become a more common attack surface.
Traditional Physical Security: Cameras, ID card scanners, etc., should be in their own network zone. This is not to be taken lightly, as the risk of a physical breach can be more harmful than a digital one. There are a number of real-world examples of this, including in 2017, the closed-circuit camera network in Washington, D.C., was hacked, leaving police cameras unable to function for three days.
Industrial Control Systems: HVAC, for example, like the non-segmented network compromised in the Target breach, should have two-factor authentication and be segmented.
Customer Databases: Due to compliance requirements, customer databases need to be secured more intently than, for instance, your print server. PCI-DSS, HIPAA, HiTRUST, FINRA, GDPR and other pieces of data legislation will determine the level of segmentation and cybersecurity that would be best practice in terms of implementation.
