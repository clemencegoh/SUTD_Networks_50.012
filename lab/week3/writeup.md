# Networks Lab 3

Name: Clemence Goh (1002075)

---
What is the normal time required to download the webpage on h1 from h2?
- Downloads in 1.0s

---
What was your initial expectation for the congestion window size over time?
- Expect that the congestion window increases over time.

---
After starting iperf on h1, did you observe something interesting in the ping RTT?
- ping RTT is much larger/longer

---
After starting iperf on h1, why does the web page take so much longer to download?
- Due to parallel streaming of data using iperf, the download channel is shared between 
streaming and downloading the web page, which means that packets sent by the web page 
will be acknowledged slower.


---
Please provide the figures for the first experiment (with qlen 100 and only one queue)
- Please comment on what you can see in the figures 




---
Please provide the figures for the second experiment (with qlen 20 and only one queue)
- Please comment on what you can see in the figures, and what is different (any why)




---






