# Week 4 - Routing and Internet Protocol


---
What is the problem anticipated by the Distance Vector
Algorithm?
- Count to infinity problem
    - concept of good news spreads fast and
    bad news travels slow
    - Once a link to a node is lost, others will 
    think that they still have a good link.
    - count to infinity in an update


How do we solve this?
- Partially, can use poisoned reversed, whereby 
distance can be set to infinity if route is 
through the node. Eg. Z tells X that its
path to Y is infinity if it reaches Y through X.
- Will not completely solve


---
Common Protocols for routing:
- Intra-AS:
    - Distance Vector, Routing Information Protocol
    - OSPF: Open Shortest Path First (LS)
- Inter-AS:
    - LS infeasible, DV or PV needed
    - BGP most commonly used PV protocol
    
    
    
---
Compare between OSPF and BGP

| OSPF | BGP |
| --- | --- |
