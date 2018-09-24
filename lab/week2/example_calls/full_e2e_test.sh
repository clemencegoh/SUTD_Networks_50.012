#!/usr/bin/env bash

# execute this only after server-side is run
# Note that server side running is dependent on path

# system variables
IMAGE_PATH=${PWD}"/examplePic.jpg"


# base path
BASE_PATH="http://localhost:8080/"
USER_PATH=${BASE_PATH}"user"
UPLOAD_IMAGE_PATH=${BASE_PATH}"images"


# variables
PROFILE_NAME="Clemence"
PROFILE_ID="1002075"


# get all current users
CURRENT_USERS=$(curl ${BASE_PATH})
echo "Current users: "$CURRENT_USERS

# create new user
curl --request POST ${USER_PATH} \
--data "Name=${PROFILE_NAME}" \
--data "ID=${PROFILE_ID}"

# get users after creating
CURRENT_USERS=$(curl ${BASE_PATH})
echo "Current users: "${CURRENT_USERS}

# get first user, ideally should be done programatically
USER_UNIQUE_ID="Clem1002"

# upload an image to user account
IMAGE_UNIQUE_ID=$(curl POST \
-F "UserID=${USER_UNIQUE_ID}" \
-F "Auth=${PROFILE_ID}" \
-F "Photo=@${IMAGE_PATH}" \
${UPLOAD_IMAGE_PATH})
echo ${IMAGE_UNIQUE_ID}

# get user details
echo $(curl ${USER_PATH}"/${USER_UNIQUE_ID}")

### cleanup

# delete image
curl -X "DELETE" ${UPLOAD_IMAGE_PATH}"/"${USER_UNIQUE_ID}"/"${IMAGE_UNIQUE_ID}"/"${PROFILE_ID}

# delete user
curl -X "DELETE" ${USER_PATH}"/"${USER_UNIQUE_ID}"/"${PROFILE_ID}

# check end state
echo $(curl ${BASE_PATH})
