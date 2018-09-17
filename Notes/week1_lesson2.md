Principles of the internet:
    - Decentralized control
    - "Best effort"
    - RESTful (stateless)

Core vs fringe:
    - core of the internet has remained more or less the same.
    - IPv6 is the latest improvement to the core

Autonomous Systems(AS):
    - A collection of IP routing prefixes 
    under one or more network operators
    on behalf of a single administrative entity or domain
    - a common, clearly defined routing policy to the internet

Internet properties:
    - Can be considered a collection of connected Autonomous Systems.

slide 11 -
!NAT: Network Address Translation 
(look this up)
Internet only needs to know IP address of gateway - not device

slide 16: IXPs  
IXPs are exchange points for ISPs of the same tier.

slide 17: DNS 
    - Domain names offer a convenient abstraction
    - Usually top-bottom, right-left. eg. (istd.sutd.edu.sg) 
    From the highest level of (sg) to the lowest level on the left of (istd).
    - See DNS record types for full list of types associated with DNS.

slide 26: Design Challenge - Addressing
    - Unique addressed are derived through separating nodes by region.


Subnet: Logical subdivision of an IP network
    - from taking IP AND Mask (logical AND)


-----> Review from slide 28 !!! <-----
- CIDR (Classless Inter-Domain Routing or supernetting)
? Subnet
? Activity 2 and 3
? Homework 1 and 2

---- After-Class Notes ----

CIDR, IPv4, and IPv6: The problem

IPv4 is a 32-bit address which came with the problem of a fixed number of identities and is hence inflexible.
For example, it provides Class A - > 16mil hosts, Class B -> 65,535 hosts, Class C -> 254 hosts. Class D addresses identify multicast domains.
This results in an organisation buying class B if it needed only slightly more than 254 host machines, which results in many IP addresses being unused, speeding up the IPv4 address pool exhaustion.

This brought about IPv6, which allows addresses to grow up to 128 bits. 

However, since this transition to IPv6 from IPv4 is slow, CIDR was introduced to provide a new and more flexible way to specify network addresses in routers.

CIDR is used to extend the useful life of IPv4.
It augments the current IPv4 to allow for the last n number of bits to be taken as the specific host address.
Address would look something like this: 192.30.250.00/18 where the number after the / is the leftmost numbers used for the network part of the address, and 32-18 being the part used for the host address.










