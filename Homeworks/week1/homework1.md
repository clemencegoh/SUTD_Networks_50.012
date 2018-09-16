# Homework 1: Learning from Ping and ICMP (Due 9/16 23:59)

<h4> Name: Clemence Goh (1002075) </h4>

**Q1. What are two advantages and two disadvantages of having international standards for network protocols?** 

Advantages: <br>
1. All computers throughout the world can be connected together due to the use of a single standard. 

2. Easily maintained by changing the standard, which will cause the inter-connected computers to install the update and change accordingly.

Disadvantages: <br>
1. A bug or vulnerability in the standard will result in an international problem instead of being confined to a nation's borders.

2. All companies must adhere to and use the standard instead of developing new methods.

---


**Q2a. Assume a host sends out a ping request using ICMP. The ICMP default payload size is 32 bytes.  Assume an ICMP header of 8 bytes and an IP header of 20bytes and an Ethernet header of size 14 bytes, What is the size of a frame transmitted on the wire?**

The size of a frame transmitted on the wire will be: <br>
32 + 8 + 20 + 14 = 74 bytes <br>
Therefore 72 bytes will be used. 

---
**Q2b. Assume that with additional ping arguments the ICMP payload becomes the maximum MTU size at IP layer (1500bytes), What is the ICMP payload size? What is the size of the frame transmitted on the wire?**

ICMP payload size = MTU - ICMP Header - IP Header <br>
  = 1500 - 8 - 20
  = 1472 bytes.

Size of frame = Ethernet header + IP Header + ICMP Header + payload size <br>
    = 14 + 1500 (MTU)
    = 1514
 
---
**Q2c. Try to verify your calculations using wireshark.**  

Wireshark: 

---

Steps: 
1) ping -l 1472 192.168.1.1 
2) Display by wireshark showing ICMP packets captured.

From wireshark, it can be seen that length of each packet is indeed 1514.




Ref: http://www.hackingarticles.in/understanding-guide-icmp-protocol-wireshark/