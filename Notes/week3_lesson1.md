# The Transport layer

Two protocols are used for almost everything.
- UDP
- TCP

---
The Socket
- Stream socket
    - logical communication between applications
- low-layer socket (raw socket)
    - logical communication between hosts

---
The Port
- Port number is a unique identifier to the specific port
- 0-1023 reserved for system only
    - only root can create sockets using these ports
    - example 22: SSH, 23: telnet, 80: http, 123: NTP
- 1024-49151 for user applications
    - registered ports for user
- 49151-65535 ephemeral ports
    - auto assigned by applications

---
UDP - User Datagram Protocol
- contains bare minimumL source _ destination port, length, checksum
- UDP header only introduces 8 bytes of overhead to any payload message
- Reliable transfer of over 98%
- However of those only 50% arrived in order

---
Connections 
- Possible to have the same destination port and IP address,
hosts will spawn a different thread for every new connection
- On a listening socket, when received a new request, spawn a new
thread.

---
Video streaming
- Commonly used is UDP for video streaming
    - Can afford to sustain loss
    - There is no need for communication
    - There is no need to make sure of delay 
    - No overhead of handshaking, ack, etc.
    
---
Checksums
- How is it calculated?
    - Add bitwise and carry. Final ans must be 4 bytes only
    - wrap around the final carry. eg. (2BBCF -> 2 + BBCF)
    - XOR against FFFF (inverse the bit)
   
---
Essential
- Sender
    - Request
- Receiver
    - Ack
- Consider:
    - How long to wait?
    - corrupted data:
        - corrupted req
        - corrupted ack
        - corrupted nack (negative ack) [No need, with timeout]
- Pipelining:
    - Sending multiple packets to fill the pipeline
    - No need to wait for first ack before waiting for next

- Types of implementation:
    - Go-back-N
    - Selective repeat

        

    
