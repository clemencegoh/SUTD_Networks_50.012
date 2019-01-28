# Homework 10 - SDN

Name: Clemence Goh (1002075)
---


**1. Simple Forwarding Behaviour:** 
- S3 entry table

| Code | Actions | 
| --- | --- |
| if dest IP == 10.2.* and ingress_port == 1 or ingress_port == 2: | send to interface 3 |

- S1 entry table:

| Code | Actions |
| --- | --- | 
| if dest IP == 10.2.* and ingress_port == 1 | send to interface 4 |

- S2 entry table:

| Code | Actions |
| --- | --- |
| if dest IP == 10.2.0.4 | send to interface 4 |
| if dest IP == 10.2.0.3 | send to interface 3 |


**2. Load Balancing:**

- S2 entry table:

| Code | Actions |
| --- | --- |
| if dest IP == 10.1.* and source IP == 10.2.0.4 | send to interface 1 |
| if dest IP == 10.1.* and source IP == 10.2.0.3 | send to interface 2 |

- S1 entry table:

| Code | Actions |
| --- | --- |
| if dest IP == 10.1.0.1 | send to interface 2 |
| if dest IP == 10.1.0.2 | send to interface 3 |

- S3 entry table

| Code | Actions |
| --- | --- |
| if dest IP == 10.1.* | send to interface 3 |



