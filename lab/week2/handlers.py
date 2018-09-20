import json
import os
import random
import re

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
    for k, _ in data.items():
        namelist.append(k)

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
    return True


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
    return os.path.join(imageFilepath(), _image)


def parseImageName(_name):
    return _name + generateRandomString(4)


def addImage(userID, imageName):
    data = getAllUserData()
    data[userID]["Images"].append(imageName)
    write_to_db(data)

def deleteImage(userID, imageName):
    data = getAllUserData()

    try:
        data[userID]["Images"].remove(imageName)

        # update database
        write_to_db(data)

        # remove from system
        os.remove(imagePath(imageName))

        return True
    except:
        print("Not found in database")
        return False


def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


def parse_filename(name):
    name = ''.join(e for e in name if e.isalnum())
    ext = "." + name[len(name)-3:]
    return name[0:3] + generateRandomString(2) + ext


# print(parse_filename("clemence i_s @ c1@s5-noW!.img"))

# print(createNewUser("Clemence","9876"))
# deleteUserHandler("Anot90")

# deleteImage("User01", "charm.jpg")
# addImage("User01","Nigj7.jpg")