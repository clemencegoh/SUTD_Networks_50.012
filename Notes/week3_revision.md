# The transport layer

--- 
What are the main issues that the transport layer 
aims at tackling?
- Transmissions between transport layers makes use of:
    - Transmitting segments and streams
    - App layer message => Converted to segments
    - Pass on to network layer for transmission
    - At receiver side, segments re-assembled on 
    transport layer and passed to application layer
    - UDP and TCP used for almost everything
- There is a need to control congestion and ensure 
reliable delivery of messages from the sensor nodes 
to the sink.
- Main challenge is throughput/congestion control.
- Loss and Re-ordering of packets received
    - high reliability, >98%
    - out of order 50% of the time


---
What has to be known beforehand to communicate
with another system at the transport layer?
- IP address
    - Identifies the host
- Port number
    - Identifies the process listening
    - Usually at most one process listens to each port
- Transport Layer Protocol used

- *Note:* Sender can choose arbitrary source port


---
How much overhead is introduced at this layer?
- UDP header introduces 8 bytes of overhead to payload.
    - Source port (2 bytes, 16bit)
    - Dest port (2 bytes, 16bit)
    - Fragment length(2 bytes)
    - UDP checksum(2 bytes)
- TCP headers consist of 16 diverse flags
    - Header length
    - unused bits
    - urgent flag
    - ACK flag
    - push flag
    - RST, SYN, FIN flags 
    - Overall: 
        - Min 20 bytes (5 words)
        - Max 60 bytes (15 words) 
    
    
---
What are the 2 solutions to transmission pipelining?
- Selective Repeat
    - individual packets having their own timeout
    and ack.
- Go-Back-N
    - in windows of a fixed size. 
    - Receiver will only send cumulative ACK
    - Sender has timeout for entire window
    - If timeout reached, send entire window again
    
---
How is congestion avoided?
- *Slow start* until loss occurs
    - *triple duplicate ACK*
        - cwnd cut by half 
        - congestion avoidance mode
        - linearly increase
    - *timeout*
        - start from 1
        - back to slow start





