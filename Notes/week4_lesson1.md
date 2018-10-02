# Network Layer

Layer 3 problems

---
NAT - Network Address Translation:

---
Network Layer provides logical connection between hosts
- Protocols: 
    - IP
    - ICMP
    - IGMP

In App layer: 
- Message

In Transport layer:
- Segment

In Network layer:
- Datagram

---
Routing Algorithm:
- Distributed algorithm throughout the net
- Collab to create routing tables
- Determines the end-to-end path

---
# CIDR

Classless Inter-Domain Routing

Slide 7:
- Subnet mask allows for changing of anything not 
within the prefix.
- Longest prefix wins in case of conflict.

# IMPORTANT

When considering subnet addresses:
- Do not use 0 and 255
    - 0 is used to address entire subnet
    - 255 is used as a broadcast

Autonomous Systems (AS)
