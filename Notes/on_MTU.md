**The ethernet MTU is 1500. Why?** <br>
 The ethernet frame has 8 byte preamble, 6 byte source and 6 byte destination mac address, mac type of 2 bytes, and 4 bytes CRC. Assuming the MTU payload to be 1500 the total number of bytes comes to 1500 + 8 + 6 + 6 + 2 + 4 = 1526 bytes. Now between each frame there is a inter frame gap of 12 bytes which constitues 9.6micro seconds gap between each frame. This is essential so that frames dont mix up. So the total size of each frame going out of a host is 1538 bytes.

---
 **MTU(Maximum Transmission Unit)** <br>
In computer networking, the maximum transmission unit (MTU) is the size of the largest protocol data unit (PDU) that can be communicated in a single network layer transaction. The MTU relates to, but is not identical to the maximum frame size that can be transported on the data link layer, e.g. Ethernet frame.

Larger MTU is associated with reduced overhead. Smaller MTU values can reduce network delay. In many cases, MTU is dependent on underlying network capabilities and must be adjusted manually or automatically so as to not exceed these capabilities. MTU parameters may appear in association with a communications interface or standard. Some systems may decide MTU at connect time.

