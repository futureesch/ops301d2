Ops301d2 - reading 12

https://www.geeksforgeeks.org/computer-network-aaa-authentication-authorization-and-accounting/

Authentication - Authorization - Accounting

Authenticate - ID of user: user-name and password; uses console port, AUX port, or vty (virtual tty) lines. Customization is at the administrator’s control
Authorize - Capabilities to enforce policies for users resource access across the network.
Accounting - Monitors and captures events processed by the user

Locally - create users for authentication and then customize privileges

ACS Server - Autoconfigure servers and seems the most common way to deploy AAA


https://wiki.freeradius.org/guide/Concepts 

RADIUS puts the client in control of the requests. Modules on the server respond to client requests if they can, otherwise it will go to the authenticator. From there, a user might include a password auth, but then the server has to have an authenticator seek the pairing on its end for a “good” password. Insufficient information can return a rejection of server requests.
