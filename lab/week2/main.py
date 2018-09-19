from flask import Flask, request
from handlers import *
import json

app = Flask(__name__)

##########
# Image storage app
##########

# This app accepts an image and stores it, returning unique ID for each image uploaded

# GET /
# returns all names of people who have uploaded their images, and a list of ids for each

# POST /user
# Create a new user

# GET /user/{id}
# returns all images from the user

# GET /images/{id}
# returns image with that id

# POST /image
# uploads a new image
# Requires user, auth

# DELETE /user/{id}
# Deletes a user and all corresponding image files
# Requires authentication

# DELETE /image/{id}
# Deletes an image of that id, requires authentication


@app.route('/')
def Hello():
    return "Welcome!"


@app.route('/students', methods=['GET', 'POST'])
def GetAllStudents():
    with open("students.json") as studentMap:
        if request.method == "GET":
            return studentMap.read()

        elif request.method == "POST":
            if request.content_type == 'application/json':
                print("json detected")
                # data = request.form.get('Name')
                print(request.json)
                return ""
            else:
                # assume plain text here
                print("Assuming plain text")
                return ""

# @app.route('/stdents')
# def GetAllStudents():
#     toReturn = "list of students:\n"
#     for key, value in studentMap.items():
#         toReturn += "{}: {}\n".format(key, value)
#
#     return toReturn





if __name__=='__main__':
    app.run(port=8080)
