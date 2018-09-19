from flask import Flask, request, abort, send_file
from handlers import *

app = Flask(__name__, static_url_path='/static')

##########
# Image storage app
##########

# This app accepts an image and stores it, returning unique ID for each image uploaded

# GET /
# returns all names of people who have uploaded their images, and a list of ids for each
@app.route('/', methods=['GET'])
def base_root():
    return str(getAllUserNames())



# POST /user
# Create a new user
@app.route('/user', methods=['POST'])
def create_user():
    _name = request.form.get('Name')
    _id = request.form.get('ID')

    if _name == '' or _id == '':
        abort(400, "Missing name and/or ID")

    return createNewUser(_name, _id)


# GET /user/{id}
# returns all images from the user
@app.route('/user/<id>', methods=['GET'])
def user_API(id):
    if id == '':
        abort(400, "No ID")

    # give to handler to resolve
    res = str(getSpecificUser(id))

    if res == "":
        abort(400, "User not found")

    return res


# DELETE /user/{id}/{auth}
# Deletes a user and all corresponding image files
# Requires authentication
@app.route('/user/<id>/<auth>', methods=['DELETE'])
def delete_user(id, auth):
    if id == '':
        abort(400, "No ID")

    if auth == '':
        abort(400, "No Auth")

    if checkAuth(id, auth):
        deleteUserHandler(id)

    return ""


# GET /images/download/{id}
# returns image with that id for download
@app.route('/images/download/<id>', methods=['GET'])
def download_specific_image(id):
    filename = imagePath(id)
    return send_file(filename, mimetype='image/gif')


# GET /images/{id}
# displays an image from its ID
@app.route('/images/<id>', methods=['GET'])
def display_specific_image(id):
    return "<img src='/static/images/{}.jpg'>".format(id)


# POST /images
# uploads a new image under user
# Requires user, auth
@app.route('/images', methods=['POST'])
def upload_image():
    print(request)

    print(request.args)

    return ""


    formData = request.form
    if len(formData) == 0:
        abort(400, "Empty form values")

    image = request.files
    if len(image) == 0:
        abort(400, "Empty image")

    print(image[0])

    userID = formData.get('UserID')
    auth = formData.get('Auth')

    if not checkAuth(_id=userID, _auth=auth):
        abort(400, "Auth failed")

    # execute the task
    addImage(userID, image[0])

    return ""


# GET image upload UI
@app.route('/images/upload', methods=['GET'])
def upload_UI():
    with open("upload_ui.html") as ui:
        return ui.read()


# DELETE /images/{id}/{auth}
# Deletes an image of that id, requires authentication
@app.route('/images/<user_id>/<image_id>/<auth>', methods=['DELETE'])
def delete_Image(user_id, image_id, auth):
    if not checkAuth(user_id, auth):
        abort(400, "Invalid authentication")

    deleteImage(user_id, image_id)
    return ""


if __name__=='__main__':
    app.run(port=8080)
