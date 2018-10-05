Q1. Consider a scenario where host addresses are 16 bits long. A router uses longest prefix matching and has the following entries in its forwarding table
Prefix   Interface

1100   Eth0

11001 Eth1

111      Eth2

Default Eth3


For each of the four interfaces, give the associated range of destination host addresses and the number of addresses in the range.

---
1)  

| Ethernet | range | number of addresses | comments |
| --- | --- | ---| --- |
| Eth0 | 1100 0000 0000 0000 - 1100 1111 1111 1111 | 2048 | Eth0 has 2^12 addresses, but 2^11 are dedicated to eth1, bringing total to 2^11 instead|
| Eth1 | 1100 1000 0000 0000 - 1100 1111 1111 1111 | 2048 | Eth1 has full range of 2^11 addresses |
| Eth2 | 1110 0000 0000 0000 - 1111 1111 1111 1111 | 8192 | Eth2 has 2^13 addresses
| Default | 0000 0000 0000 0000 - 1111 1111 1111 1111 | 53248 | default covers everything else, 2^16 - 2^13 - 2048 * 2


---
Q2. Consider a subnet with prefix 10.20.15.128/26. 
Give an example of an IP address (of the form xxx.xxx.xxx.xxx) that can be assigned to this network. 
Suppose an ISP owns the block of addresses of the form 10.20.12.0/22. 
Suppose it wants to create two subnets from this block, with each block having the same number of IP addresses. 
What are the prefixes (of the form a.b.c.d/x) for the two subnets?

---
2)

a) Example: 10.20.15.129

b) 10.20.12.0/23 and 10.20.14.0/23



