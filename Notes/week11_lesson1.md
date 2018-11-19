# RECAP

What increases network performance?
- Caching
- Compression
- Content Distribution Networks
- Proxies
- Multicast of streaming traffic


---
Techniques of redundancy: **VIDEO**
- Spacial
    - Pixels are the same color, no need to re-send
    - **WITHIN IMAGE**
- Temporal 
    - Between 2 images, not much difference
    - Only send the pixels that are different
    - **INTER IMAGE**
    
    
---
3 Different key types:
- Stored audio/video
- Conversational voice/video
- Streaming live audio/video

---
Types of streaming:
- UDP:
    - Need overlay network
    - Requires Real Time Transport Protocol
    - Need to match transmission rate with client's consumption rate
    - Required separate out of band control through Real Time Sequencing Protocol
    - Blocked by firewalls
- Http Streaming:
    - Most commonly used
    - TCP based, with congestion control
    - Delay is a problem
    - Can go beyond firewall
    - Youtube, Netflix,...
- Adaptive Http
    - Allow multiple versions of audio and video to 
    adapt to client capability
    
---
Streaming stored video:
- Network has to add random delays when received to prevent client side streaming
from catching up to rate at which it is being uploaded


Streaming Multimedia: **DASH**
- Dynamic
- Adaptive
- Streaming 
- over HTTP
    - IDEA:
    - **Server** divides video file into multiple chunks
        - chunks stored and encoded at different rates
        - each chunk tied to different URLs
    - **Client** periodically measures mandwidth
        - Consult manifest and download 
    
---
    

    
    
    





