# Week 2 revision - Application Layer

---
How does the application layer interact with the
transport layer?
- Sockets allow for multiplexing requests from 
application to transport layer and vice versa


---
What are the protocols within the application layer?
- File Transfer Protocol (FTP)
- Simple Mail Transfer Protocol (SMTP)
- HTTP with HTML and image content
- Skype for audio/video chat


---
What are the "good to haves" for a message protocol?
- Message integrity check
    - verify content
- Good throughput
    - Receive large messages
- Low transmission delays
    - Near real time
- Security
    - Make sure that no one else can eavesdrop
    - Done over the Transport Layer Security (TLS)
    over TCP


---
What are the REST principles?
1. Statelessness
2. Cacheability
3. Layered system
    - cannot ordinarily tell if it is connected
    directly to the end server.
4. Code on demand
    - servers can temporarily extend or customize
    functionality of a client by transferring 
    executable code. (Java applets, Javascript)
5. Uniform Interface
6. Client-Server Architecture

---
What are the main motivations behind using REST?
- Scalability
- Generality
- Independence
- Latency
- Security
- Encapsulation

---
What are the motivations behind using JSON?
- Ubiquity
- Simplicity
- Readability
- Scalability
- Flexibility

---
Why do we need web caching?
- Reduce response time for client request
- reduce traffic on the institution's access link
- cache can act as both client and server
    - server: for original requesting client
    - client: to origin server



