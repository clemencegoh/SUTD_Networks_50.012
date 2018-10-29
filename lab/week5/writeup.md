# Lab 5 - Network

Name: Clemence Goh (1002075)
---
**Brief description of the network setup provided:**
- **IP subnet for the desktops and server**
- **Which server is acting as DHCP server**
- **What you had to fix in the DHCP setup to reach 8.8.8.8**

---
- 


- To fix the DHCP setup, change config file's 
`dhcp-option:3` address from `10.0.0.111` to `10.0.0.1`. 
This is to correctly route the packets through intGW.

---
**Why can you resolve nils.net? Briefly describe where from h1 knows
about a DNS server, and what its IP is.**

---
nils.net has an IP of 8.8.8.2



---
**Who is doing the NAT'ing? Which address ranges it is translating
between?**

---
IntGW is doing the NAT'ing.

Address ranges:
- 


---
**Did you manage to block srv1 from reaching the outside world?**

---

---
**Did you do any of the optional tasks?**

---

---