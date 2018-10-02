# Optimization of Network

Routing Continued:
- Link state routing
    - Dijkstra's algorithm 
    - In O(|E|*|V|)
        - Since each router sends cost information for all neighbours:
            - Does not scale on the internet
            - |E| and |V| are huge -> product bigger
            - Need to build on local information
    - Distance Vector algorithm is required.
        - Dynamic programming
        
---
Infinity problem:
    - If a connection is dropped:
        - A still thinks he can get to C through B
        - B thinks he can through A
        - End state, send to each other through infinity
    - Solution:
        - When route fails, Distance vector protocol
        spreads the bad news by poisoning the route.
        - Poisoning sets the route metric value at infinity.
        - 
        
        
        
---
Inter-AS routing
- Since the sheer number of nodes are huge, LS is infeasible (link state)
- DV or PV needed
- BGP is the most commmon Path Vector protocol


