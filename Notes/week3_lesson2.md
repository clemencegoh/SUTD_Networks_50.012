# TCP, Transport Control Protocol

connection management:
- RST (reset)
- SYN (Sync)
- FIN (finish)

---
Triple duplicate Ack
- Sends multiple in pipeline
- Receiver sends nack for packets received out of order
- After 3 duplicate nacks, sender resends missing packet

---
FIN requires both sides to send FIN message.
- This is due to one side possibly doing book-keeping

Optimising of sending data
- Slow start mode
    - starts in this mode to test the TCP connecgion
    - increases exponentially (power of 2)
- Congestion avoidance mode 
    - after first dropped ACK
    - drops to half from start of congestion
    - increases linearly

- connection starts in slow mode and increases exponentially
until congestion is detected
    - if timeout: **(TCP Tahoe)**
        - reset and start from 1 again
    - if 3 duplicate ACK: **(TCP Reno)**
        - cut to half of start of congestion and increase 
        linearly

- slow start increases until it hits **ssthresh**
- ssthresh set to 1/2 of cwnd just before loss event
- very first ssthresh is determined by increasing cwnd all the way
until a loss is reached, set ssthresh = 1/2 cwnd


