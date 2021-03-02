https://www.howtogeek.com/194069/what-is-a-windows-domain-and-how-does-it-affect-my-pc/ 

Domains are used to create a local network name for a server to operate from as a controller to the network pcs. 

Usernames and accounts are stored on the server so users can log in from any machine on the network - also possible thru VPN and the Internet

Group Policy Settings can be managed from one computer to affect all regardless of changes in local settings (the changes probably won’t be visible or permitted, requiring admin access to change), effectively locking down the computers managed by the DC.

Only Windows Pro machines can be attached to domains since they are intended for enterprise, and not home use.

Workgroups are the default and are not domains; instead, they are simply computers on the same LAN. No one PC controls another as they are equals on the network and in the workgroup. No passwords are needed. As an older Windows feature, their main function today is to make network file sharing easier.

Domains usually limit what can be done on a given machine for standardization, security, and other specialization needs. Leaving a domain is atypical for a user, but typical for sysops folks in setup, on- and off-boarding.
