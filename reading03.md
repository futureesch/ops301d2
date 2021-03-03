https://www.cyberark.com/what-is/active-directory/ 

Microsoft Active Directory is their proprietary moniker for Windows domain networks. This service helps IT admins manage Identity and Access to assert control over:
Single-sign on (SSO) integrates all user logins alleviating password fatigue and helps streamline functions for security.
Multi-factor authentication (MFA) requires two methods of verification like a login and a fingerprint or a rotating token to a trusted to device perhaps via SMS
Provisioning and Life-Cycle provides the sysadmin with tools to empower the user for requests to minimize help desk requests, on- and off- boarding of employees, as well as monitoring tools
It is also conceptualized as IDaaS

There are five variations of the Active Directory depending on business need, though it’s really about AD DS vs. AD LDS and then the additional service options certification, rights, and management.

“Fundamental Active Directory features and capabilities include:

A schema that defines the classes of objects and attributes contained in the directory.
A global catalog that contains detailed information about every object in the directory.
A query and index mechanism that allows users, administrators, and applications to efficiently find directory information.
A replication service that disseminates directory data across the network.”

“Active Directory makes use of other security and networking protocols including LDAP (Lightweight Directory Access Protocol), DNS (Domain Name System), and Microsoft’s version of the Kerberos authentication protocol.”

“Active Directory Domain Services Overview

Active Directory Domain Services is the primary Active Directory service. 
It is used to authenticate users and to control access to network resources. 
A server running AD DS is called a domain controller. 
Most Windows domain networks have two or more domain controllers; a primary domain controller and one or more backup domain controllers for resiliency. 
During login, users authenticate to a domain controller and are granted access to particular resources based on administratively defined policies.”

Domain is a collection of objects--users and devices--sharing the same database

Trees would be like sales.company.com, returns.company.com, marketing.company.com, payroll.company.com, etc.

Forests would be all of those trees mentioned who share the DNS company.com

“Active Directory Benefits

Security – Active Directory helps businesses improve security by controlling access to network resources.
Extensibility – companies can easily organize Active Directory data to align with their organizational structure and business needs.
Simplicity – administrators can centrally manage user identities and access privileges across the enterprise, helping businesses simplify management and reduce operations expenses.
Resiliency – Active Directory supports redundant components and data replication to enable high availability and business continuity.”


“Relationship to Azure Active Directory

Azure Active Directory is Microsoft’s next-generation, cloud-based identity management solution used to control access to SaaS solutions like Microsoft 365 (Office 365), internally developed cloud apps running on Azure, as well as traditional enterprise applications and other on-premises resources. It adds support for just-in-time access controls, multi-factor authentication and passwordless technologies, native mobile-device management, and identity federation standards like SAML and Oauth2, among other capabilities.

CyberArk Idaptive integrates with both Active Directory and Azure AD and enables you to provide Single Sign-On, Multi-Factor Authenticaiton, and Lifeycle Managemenet capabilities for users stored in these directories.”


