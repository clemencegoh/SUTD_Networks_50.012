# Enterprise Networks

What's different:
- Has professional support for users and systems
- High requirements on availability of services.

---
Switches in SDN:
- Everything is a generic packet switch, no such thing as 
layer 2 or layer 3
- This is at the control plane

---
**Internal Routing** - Multiple campuses
- Routing between campuses or internal
    - Due to firewall reasons
    - Firewalls are usually done at layer 3

Recap: **DMZ(demilitarised zone)**:
- anything that has to be front facing, not sensitive
- email
- web server
- strictly no DB

Network Access Storage **NAS**/ Backup:
- Tapes (?) old tech
    - large storage, cheap
    
    
---
Web Proxies:
- Allow Private IP addresses **(Specific)** to access the internet

Firewall:
- Traffic routed through a firewall

Network Time Protocol (NTP)

 
Management of networks
---
Mainly concerned with:
- Fault
- Config
- Accounting
- Performance
- Security


SNMP (Simple Network Management Protocol)
---
**SLIDE 24-26**
- Has both polling and interrupt
    - This depends on what is needed
    
    
Case study: Slide 33
---
- Cons:
    - Single point of failure
    - Entire cluster is a link layer broadcast 
    - Needs a border router between NAT and provider router
    - Router instead of switch in the centre to separate subnets
        - Routes between internal services, staff, and students
    - Need a DMZ right beside BGP, which allows public to 
    access 
    - Security is a problem: Needs Firewall at DMZ
        - Will prevent all other traffic except for mail, web
        server, and DNS.
    - Might need firewall at Router for rest of enterprise:
        - Protects against stray packets
    - Against insider attacks: firewall from Router to switches
    - IDS and IPS also (slide 37)
    - Redundancy should be available in case of failure (double BGP)
    


