# Token Bucket

Name: Clemence Goh (1002075)
---

a and b. timeslot, queue, output

| Timeslot | Packets in Queue | Output | Number of tokens in bucket |
| --- | --- | --- | --- |
| 0 | 1, 2, 3 | - | 2 | 
| 1 | 3, 4 | 1, 2 | 1 |
| 2 | 4, 5 | 3 | 1 | 
| 3 | 5, 6 | 4 | 1 |
| 4 | 6 | 5 | 1 |
| 5 | - | 6 | 1 |
| 6 | 7, 8 | - | 2 |
| 7 | 9, 10 | 7, 8 | 1 |
| 8 | 10 | 9 | 1 |
| 9 | - | 10 | 1 |