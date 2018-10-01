# Week 2 lesson 1
# The Application Layer

Relies on lower layers to provide routing,
error correction, etc.

---
Examples of application layer protocols:
- SMTP
- Transport Layer Security (TLS)
- Domain Name Service (DNS)
- Secure Shell (SSH)
- Telnet (Teletype Network)
- Skype traffic for audio and video chat

---
Sockets
- Object that you can read/write/listen on
- IP address with port is known as a socket.
- Endpoint used for communication flow between 
2 programs over a network.
- Applications create the socket with 
lower layer information.

In-Betweens:
- TLS (Application layer)
    - Used to provide msg authentication,
    confidentiality and integrity
    - Used to improve security of app layer
    protocols
- TCP (Transport layer)

---
- Segmentation and Reassembly
    - This is done to prevent large amounts of packet loss 
    at a time, since the smaller the packets, the less the
    amount of data loss when packets are dropped.
    
---
- TCP vs UDP
    - The main difference is that UDP does not require a 
    confirmation
    - Sockets will be different. Listening socket is same,
    but request is served using a different socket for each
    client.
    - After data is sent, listening socket is kept alive, 
    sending socket is closed.
    
    
What are Protocols?
- Generally define 4 aspects:
    - Type of message
    - Message syntax
    - Message semantics
    - Rules
    
File Transfer Protocol (FTP):
- Connection oriented protocol
- Only understands getting files, not folders
- Important differences between 
Hyper Text Transfer Protocol (HTTP):
    - Not transcient, remains until client disconnects

HTTP:
- Uses TCP
- Is "Stateless"
    - Use Representational State Transfer (REST) API
    - GET, POST, PUT, DELETE
    - Idempotency and side-effects (Change in state)
    - Cookies maintain state in an otherwise stateless
    environment
    
    
BitTorrent:
- Works due to high rate of upload = high rate of download.
- This results in a peer 2 peer network.
- Optimistic unchoking (Spreading the work to reduce load on 
any one machine)
    - This causes the paired machines to become each other's 
    "top 4 providers"
