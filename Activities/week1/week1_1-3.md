**Activity 1** <br>
According to one source there are fifty billion nodes predicted to be on the Internet by the year 2020. (See https://www.electronicsweekly.com/news/business/information-technology/fifty-billion-internet-nodes-predicted-by-2020-2013-01/  ) It is estimated that the Internet is doubling approximately every 18 months. What is the estimated size of the Internet (in number of nodes) in the year 2029? Do you think this estimate is reasonable? Why or why not?

---
*Answer:* 

3200 billion
Not reasonable, since we only have 7 billion people in the world. We will probably not require that many nodes.

---
**Activity 2**<br>
Find out information about the company abracadabra.com using mxlookup, monitis or software on your computer such as dig / nslookup.

Find out the following details:

- IP address
- Using the IP Address use mxlookup to do an Reverse DNS lookup – do you get the same domain name? Can you explain your answer? 
- Which is their primary DNS server
- Which is their authoritative name server?
- Could you find more than one? How can you explain it?
- Find out the ASN of the AS that the domain belongs to
- Find out email gateway(s) if possible
- Find out security related information (keys, Hashing algorithms etc.)

---
*Answer:* 

1) 159.65.37.60
2) No, got classic50.allwebnow.com instead. This must be the domain pointer for abracadabra.com
3) primary server: ns1.allwebnow.com
4) Authoritative name servers:
    - ns1.allwebnow.com
    - ns2.allwebnow.com
    - ns3.allwebnow.com
    - ns4.allwebnow.com
5) Yes, there are multiple authoritative name servers. This is to ensure failovers, such that the domain is still functions even with one more more servers down at a time, due to overloading or other reasons.
6) ASN is AS14061
7) Email gateway: systemnotifications.preciselymanaged.com 
8) None available


-----------------------------------------------
**Activity 3**<br>
If I want just one device to be on the network, can I set the subnet mask to 255.255.255.255? For example, consider the following configuration:
- IP address 10.0.0.10 
- Subnet mask 255.255.255.255 
- Gateway 10.0.0.1 

10.0.0.10 will be the only device in the network talking to the 10.0.0.1 gateway? Is there a problem with this configuration? If no, explain. If yes, can you fix the problem.

---
*Answer:* 

Yes, there is a problem with the configuration.
By setting the subnet mask to 255.255.255.255, this indicates that there is nothing else within the subnet. Since there is a gateway present, there are 2 devices present, and the gateway needs to be in the same subnet as the device.
A better solution would be to set the following configuration:
- IP address 10.0.0.2
- Subnet mask 255.255.255.252
- Gateway 10.0.0.1
 
