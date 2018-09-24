Try out the following on using python on your laptop along with the requests library (you may need to use python3):
>>> r = requests.get(’https://api.github.com’)

>>> r.status_code

>>> r.headers[’content-type’]

>>> r.encoding

>>> r.text

>>> r.json()
Now try to include authentication using the following (print out the same fields of the returned object r) :
>>> r = requests.get(’https://api.github.com/user’, \        auth=(’user’, ’pass’))

What do you get? Can you explain?  Submit your answers below or in a separate file attachment.

---
Without auth, returns 200 since it is a valid request, and returns content as per normal.
With auth, since 'user' and 'pass' are not valid, it returns 4xx.
With a valid username and password, it returns 2xx.
With a valid username and password, but 2FA protected, it returns 4xx.