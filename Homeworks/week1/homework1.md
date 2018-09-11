Homework 1: Learning from Ping and ICMP (Due 9/16 23:59)

Q1. What are two advantages and two disadvantages of having international standards for network protocols? 

Advantages:
1. All computers throughout the world can be connected together due to the use of a single standard. 

2. Easily maintained by changing the standard, which will cause the inter-connected computers to install the update and change accordingly.

Disadvantages:
1. A bug or vulnerability in the standard will result in an international problem instead of being confined to a nation's borders.

2. All companies must adhere to and use the standard instead of developing new methods.




Q2a. Assume a host sends out a ping request using ICMP. The ICMP default payload size is 32 bytes.  Assume an ICMP header of 8 bytes and an IP header of 20bytes and an Ethernet header of size 14 bytes, What is the size of a frame transmitted on the wire? 












Q2b. Assume that with additional ping arguments the ICMP payload becomes the maximum MTU size at IP layer (1500bytes), What is the ICMP payload size? What is the size of the frame transmitted on the wire?





Q2c. Try to verify your calculations using wireshark.  




Ref: http://www.hackingarticles.in/understanding-guide-icmp-protocol-wireshark/