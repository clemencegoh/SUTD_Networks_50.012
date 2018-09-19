import json
import os
import random

def generateRandomString(_length):
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numString = "1234567890"
    allPossible = alphaLower + alphaUpper + numString

    toReturn = ""
    for i in range(_length):
        toReturn += random.choice(allPossible)
    return toReturn


def getAllUserData():
    with open("userdata.json") as userdata:
        data = json.loads(userdata.read())
        return data


def getAllUserNames():
    data = getAllUserData()
    namelist = []
    for _, v in data.items():
        namelist.append(v['Name'])

    return namelist


def getSpecificUser(id):
    try:
        userdata = getAllUserData()
        return userdata[id]
    except:
        return ""


def generateUID(_name, _id):
    return _name[0:4] + _id[0:4]


def createNewUser(_name, _id):
    data = getAllUserData()

    generatedID = generateUID(_name, _id)

    data[generatedID] = {
        "Name": _name,
        "ID": _id,
        "Images": []
    }

    write_to_db(data)

    return str(generatedID)


def checkAuth(_id, _auth):
    data = getSpecificUser(_id)
    if data == "" or data['ID'] != _auth:
        return False
    return False


def deleteUserHandler(_id):
    data = getAllUserData()
    del data[_id]
    write_to_db(data)

def write_to_db(_dict):
    with open("userdata.json", "w") as userdata:
        userdata.write(json.dumps(_dict))


def imageFilepath():
    cwd = os.getcwd()
    return os.path.join(cwd, "static", "images")


def imagePath(_image):
    return os.path.join(imageFilepath(), _image + ".jpg")


def parseImageName(_name):
    return _name + generateRandomString(4)


def addImage(userID, imageName):
    name = parseImageName(imageName)
    data = getAllUserData()
    data[userID]["Images"].append(name)
    write_to_db(data)

def deleteImage(userID, imageName):
    name = parseImageName(imageName)
    data = getAllUserData()
    data[userID]["Images"].remove(name)
    write_to_db(data)


# print(createNewUser("Clems","120005"))
# deleteUserHandler("Anot90")