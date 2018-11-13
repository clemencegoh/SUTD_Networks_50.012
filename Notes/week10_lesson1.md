# Lecture 15 - Wireless Mesh Networks

Router/Node Interface - ???

**Remember that wireless nodes have limited range**

Ad-hoc on demand Distance Vector (AODV)
- Only starts algorithm when another node needs to be reached
- Built on the fly
- For small ad-hoc networks
- Stores in **routing table**

---
Path discovery
---

See slides 15 onwards
- Generally want to set a TTL (hop count) to a small number 
so the number of broadcasts are limited 
(otherwise creates large amount of congestion in large networks)
- 


---
Mesh Architecture:
---
Everything is wireless within except of mesh portal point
- Increase number of mesh portal points to reduce 
load on bottleneck
- Look at slide 35 for full architecture, of how mesh AP and 
mesh points interact with Mesh gateway/portal point and
non-mesh client (end user)
- Link layer forwarding


Difference: Hybrid Wireless Mesh Protocol
- slide 39


---
Personal Notes
---

Ad-hoc on-demand Distance-Vector Routing (AODV):
- Reactive/on demand
- descendant of DSDV
- bi-directional links
- Route discovery cycle used for route finding
- maintains **active** routes.
    - uses *"lifetime"* to determine if route is active
- Sequence numbers used for loop prevention and route 
*freshness* criteria.
- Provides Unicast and Multicast
- Discards unused routes
- can determine multiple routes, but keeps only a single
one. 
    - too much book-keeping involved
    - difficult to manage multiple routes between same 
    source/destination pair
    


