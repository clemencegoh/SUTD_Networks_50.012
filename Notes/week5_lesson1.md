# Kurose & Ross chapter 5 slide set
# The Link Layer

- MAC address - Medium Access Control
- Ethernet - most widely used wired technology
- ARP - Address Resolution Protocol

- Switches revised
- VLANs

---
How to put information on routers to forward addresses?
- Routing Protocol
- Data Linked Layer is concerned with each hop in this
routing protocol.

| LAN/WAN wired | Wireless/Wifi |
| --- | --- |
| Collision hard to happen | Collision could happen |
| **Point to point** | **broadcast** |


Link Layer Services
--- 
- Flow contol:
    - pacing between adjacent sending and receiving nodes
- Error detection:
    - Errors caused by  signal attenuation, noise.
        - Solution is to do error correction at each hop
        - This is to ensure that instead of asking for
        the ack through the entire path again, ask for that
        one hop only instead.
        - This is error correction at the data link layer
    - Receiver detects pressence of errors:
        - signals sender for retransmission or drops frame
- Error correction:
    - Receiver identifies and corrects bit errors without resorting
    to retransmission
- half-duplex and full duplex:
    - with half duplex, nodes at both ends of link can transmit, but
    not at the same time
    
Adaptors
---
- Adaptors encapsulate data into datagrams to transfer to the next
layer

Ethernet
---
- Similar to UDP, connectionless (no handshakes)
- Unreliable - No retransmission protocol
    - cyclic redundancy checksum allows error detection
- Medium Access - Wired Ethernet can handle collisions
- Shared medium is a problem due to collisions
    - Can be solved with transfer protocols

IP layer - Most important **32 bit IP Addresses**
- Headers:
    - 8 byte preamble
    - 6 byte destination addr (48 bit)
    - 6 byte source addr

What is ARP?
---
- Give it a IP address, get MAC address
- Identify uniquely the particular host
- Hex number MAC
- function of ARP is used locally to get the host of MAC within
the same subnet

What are switches for?
---
- Finds out MAC addresses
- If MAC address comes in that is not found in the table,
drops it.
- **Filtering**
    - only if entry is found for destination and if destination 
    is alr on segment, then drop frame.
    - Otherwise, if destination is not on segment, flood










