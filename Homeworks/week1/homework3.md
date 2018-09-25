Continued from Activity 5:

Name: Clemence Goh (1002075)

After the 25th transmission round, segment loss is detected by timeout.

•  Plot the graph from transmission rounds 26 to 30.
   - See attached
    
•  What is the initial value of ssthresh at the first transmission round?
   - Initial ssthresh: 29 segments (slightly above 28)
    
•  What is the value of ssthresh at the 23rd transmission round?
   - 22 segments (half of 44)
   
•  What is the value of ssthresh at the 29th transmission round?
   - 14 segments (half of the cwnd at loss event)
   
•  During what transmission round is the 75th segment sent?
   - 7th transmission round
   
•  Assuming packet loss is detected after the 30th round, by receipt of a triple duplicate ack, what will be the values of the congestion window size and of ssthresh?
   - cwnd size: 8 segments
   - ssthresh: 4 segments
   
•  Suppose TCP Tahoe is used (instead of TCP Reno), and assume that triple duplicate ACKs are received at the 20th round.  What are the ssthresh and congestion window size at the 23rd round?
   - ssthresh: 22 segments 
   - cwnd: 1
   
Please submit your plot and answers on eDimension. An enlarged copy of the starter graph from Activity 6 is available on eDimension.