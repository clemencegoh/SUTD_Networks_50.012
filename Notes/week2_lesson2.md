GET, POST, PUT, DELETE

---
Safe Methods: (No side effects on resources in server)
- GET, HEAD

Idempotent methods: (Executed multiple times with same end state)
- DELETE, PUT

Non-idempotent: (end state reliant on number of times called)
- POST


URI 
- Uniform Resource Identifier
- Unique ID of resource

URL
- Uniform Resource Locator
- ID + location of resource

URN
- Uniform Resource Name
- ID + persist in time (eg. after deletion)

---
Proxies:
- Both server and clients can use proxies
- For Clients:
    - Private IP when browsing
- For Server:
    - Multiple proxies to disallow attacks/keep server
    up if one fails.
    


