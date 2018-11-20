# 

Need to police the traffic
- 3 possible insights into how to segregate the traffic:
    - 
    
    
Traffic isolation
- While maintaining a priority queue, there should be a small amount
of bandwidth reserved for the lower priority.


Types of queuing mechanisms:
- Priority
- Round Robin
- Weighted Fair Queueing (WFQ)


Leaky Bucket:
- Input => Bucket => Output
- This allows for bucket to hold on to extra inputs
and "leak" at a fixed rate.
- Disadvantage of this is that the output rate is fixed.
    - This means that is is possible to have the bucket fill
    up endlessly. 
- Leaky bucket drops packets

Token Bucket:
- Input size is fixed. 
- Output size can be variable
- Bucket holds up to b tokens
- The other packets not given a token have to wait in queue
- Advantage is that token buckets can send large bursts
- Token bucket drops tokens, not packets







    