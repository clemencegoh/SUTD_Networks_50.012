import requests


BASE_PATH = "http://localhost:8080/"


def GetAllUsers():
    return requests.get(BASE_PATH)


def CreateNewUser(_name, _id):
    return requests.post(BASE_PATH + "user", {
        "Name": _name,
        "ID": _id
    })


def GetUserDetails(_uid):
    return requests.get(BASE_PATH + "user/" + _uid)


def DeleteImage(_uid, _imageID, _auth):
    return requests.get(BASE_PATH +
                        '/images/{}/{}/{}'.format(_uid, _imageID, _auth))



if __name__=='__main__':
    pass