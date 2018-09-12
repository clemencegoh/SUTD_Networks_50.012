# 50.012 - Networks

Name: Clemence Goh (1002075)

**Local Machine IP address:** 10.12.44.205 <br>
**Mask:** 255.255.0.0


**Using tracepath estimate on the 'border' between SUTD network and the internet:** <br>
118.201.75.169 is the address of the 'border'. 


**Example for a link through an underwater cable:** <br>
ams.ix.nl.plusline.net


**Experience link loss? Why?** 

Yes. The presence of "no reply" when doing a traceroute could indicate either a packet loss at those locations, or a restriction by the company at those IP addressed to block ICMP calls. Another possible source of link loss could be due to congested links, where packets are dropped.

**Brief summary of experience with the LAN setup using the switch. What worked and what did not work?** <br>
The switch allows computers that are connected to it to form a network. This allows each computer to ping the other and receive a response, which means that they are communicating. Something that did not work was the attempt at assigning the same IP address to different computers. In this case, the IP address in question was assigned to the last computer since this assignment overrides the previous assignments made to the computers who had claimed the IP address earlier.

