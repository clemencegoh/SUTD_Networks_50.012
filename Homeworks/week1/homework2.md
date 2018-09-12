# Homework 2: IP Addressing (Due 9/16 23:59)

Name: Clemence Goh (1002075) 

---

Q1. The subnet mask for a particular network is 255.255.31.0 Which of the following pairs of IP addresses could belong to this network ? 

(a) 172.57.88.62 and 172.56.87.23.2

(b) 10.35.28.2 and 10.35.29.4

(c) 191.203.31.87 and 191.234.31.88

(d) 128.8.129.43 and 128.8.161.55

---
**Answer: b) and d)** 

The pair of IP addresses which could belong to the network are: <br>
10.35.28.2 and 10.35.29.4 <br>
128.8.129.43 and 128.8.161.55

**Reason:** <br>
a) and c) are eliminated since the second byte should not be different.

The third byte of the mask is 0001 1111

b) 10.35.(0001 1100).2 and 10.35.(0001 1101).4 <br>
d) 128.8.(1000 0001).43 and 128.8.(1010 0000).55 <br>

since the mask affects the 5 rightmost bits, both b) and d) contain IP addresses which could belong to this network. 