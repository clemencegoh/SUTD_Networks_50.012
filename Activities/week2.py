import requests
from util import documentInFile

def activity2(name, r):
    filepath = "D:\\desktopStorage\\school\\SUTD_Networks_50.012\\Activities\\generated\\" + name
    documentInFile(filepath, 'r.status_code', r.status_code)
    documentInFile(filepath, repr(r.headers['content-type']), r.headers['content-type'])
    documentInFile(filepath, repr(r.encoding), r.encoding)
    documentInFile(filepath, repr(r.text), r.text)
    documentInFile(filepath, repr(r.json()), r.json())

def activity2_noAuth():
    r = requests.get('https://api.github.com')
    activity2("wk2_NoAuth.md", r)

def activity2_Auth():
    r = requests.get('https://api.github.com/user',
    auth=('user', 'pass'))
    activity2("wk2_Auth.md", r)


if __name__=='__main__':
    # activity 2 auth and no auth below
    activity2_noAuth()
    activity2_Auth()
