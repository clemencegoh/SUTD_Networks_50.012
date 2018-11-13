# Review Questions for Week 1 

---
What are the fundamental network protocols?
- User Datagram Protocol (UDP)
    - used for broadcasts, not expecting reply
    - sending of data in a download video
- Transport Control Protocol (TCP)
    - Used for a consistent connection
    - Video calls, with 2 way transfer
- Internet Protocol
    - tasked to deliver packets from source host
    to the destination host based on IP address

- Domain Name System/Space:
    - A, AAAA, CNAME, etc.

- ARP: Address Resolution Protocol
    - Protocol for discovering link layer address
    - MAC address (IPv4)


---
What are the reasons for having a variety of different
types of networks?
- Different requirements:
    - WAN
    - LAN
    - Each of these require either high reliability 
    or high speed. Protocols change accordingly.


---
What are the five network layers:
- application
    - messages (json format most common)
- transport
    - segment 
    - (port numbers, flow control, integrity checks)
- network
    - datagram
    - IP addresses
- data link
    - frame
    - MAC address, checksums, channel access data
- physical
    - Symbols
    - translation from digital to analog
    
    
---
What is a subnet mask?
- Subnet masks allows better use of addresses.
- This is due to many IP addresses left unused.
- For example, 10.0.2.1/30 denotes first 30 bits
being subnet, allowing 4 local IPs.
- Therefore, subnet consists of host+netmask.




