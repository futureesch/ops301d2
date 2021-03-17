Ops301d2 - reading 04

https://www.lepide.com/blog/what-is-group-policy-gpo-and-what-role-does-it-play-in-data-security/ 

Group Policy in Windows numerous advanced settings for network administrators “to control the working environment of users and computer accounts in Active Directory.” Centralizes configuration operating systems, applications and users’ settings, and other administrative management tools.

When used correctly, they can simultaneously protect users from within and from without.

Using Microsoft Management Console (MMC) Group Policy Editor, GPOs can link to one or many Active Directory “containers,” such as sites, domains, or organizational units (OUs). MMC empowers users to make GPOs to define “registry-based policies, security options, software installation,” etc..

Active Directory GPOs logical order; local policies, site policies, domain policies and OU policies. “Note: GPOs that are in nested OUs work from the OU closest to the root first and outwards from there.”

GPOs help to ensure data and core IT infrastructure is set up in a secure way. Because Windows has vulnerabilities out of the box, GPOs can help close these openings.

Policies like “least privilege” are designed to protect users from logging activity that could get them in trouble; instead, focus on their jobs. Outdated protocols can be identified and disabled.

Benefits to password policy in establishing length, complexity, and other requirements to prevent brute force attacks; systems management saves hours of time onboarding new users with GPOs that guide their first experiences with the network;GPOs that check the overall health of the system for updates and patches to assure latest protection 

A few limitations include
GPO editor console is rough; adept PowerShell may really make it easier, but at the price of knowing advance PS
Be sure updates are set past 0 minutes, otherwise the GPOs will attempt to update every 7 seconds!
Cyber attacks can change GPOs to acquire lateral access, so Group Policy auditing and monitoring solutions are recommended for bigger businesses.
