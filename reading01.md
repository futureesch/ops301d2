https://www.howtogeek.com/404763/whats-the-difference-between-windows-and-windows-server/ 

The similarities between Windows 10 and Windows Server share basic platforming, however the intention for each computer differs greatly in that the former is for individual users to sit in front of, whereas the server is meant to provide services to a variety of users. 

Windows Server 2016 is designed to work better without a GUI to reduce the overhead needed. This is likely to change as virtualization takes over all areas of computing - case in point: I just got a Synology DS720+ and the interface for using it is web-based and GUI-supported. It makes setting up a plex server stupid easy. 

Further proving the point is how the rest of the article focuses on the Windows Server 2016 experience through the GUI, despite mentioning its GUI-less efficiency and intention!

With the GUI, it is easier to select the services you wish the server to provide: Windows Deployment Services, DHCP Services, and Active Directory Domain Services “allow deployment of an OS remotely to other machines, the creation of static IP address for client machines, control of a network domain for joining other computers to a domain, and creating domain users.”

https://www.howtogeek.com/school/windows-network-sharing/lesson8/ - goes into more depth re: SMB Direct (for faster file-sharing)

Server computers are designed to be workhorses capable of handling larger hardware storage and ram capacities. “Windows 10 has a limit on processors as well. The Windows 10 Home edition only supports one physical CPU, while Windows 10 Pro supports two. Server 2016 supports up to 64 sockets. Similarly, a 32-bit copy of Windows 10 only supports 32 cores, and the 64-bit version support 256 cores, but Windows Server has no limit for cores (emphasis my own).”

Windows Server is locked down - limited access to the Internet with legacy IE produces painful, recurring pop-ups blocking the way to even downloading a separate browser--you just don’t browse the web with your Server, unless you really know what you’re doing.

Setting up a domain account https://www.howtogeek.com/194069/what-is-a-windows-domain-and-how-does-it-affect-my-pc/ is crucial to accessing Windows Server as an admin since 365 does NOT port over.

The article states the obvious that Windows 10 is a familiar Desktop experience, more open to the web, bloated, and ways to make Windows 10 feel like 7.

Windows Server licenses aren’t easy to buy like a PC product key for 10. They are designed for business. Then somehow, the author tries to argue this is the choice for home needs too...
