import argparse
from flask import request
import flask
from flask_cors import CORS
import base64
import json
from smokerAlgo import smokerALgo
import os
import instagram_api
import cv2
import numpy as np
#rf = Roboflow(api_key="Tao36WXLMwnYXJt3uFaj")
#project = rf.workspace("cigarette-c6554").project("cigarette-ghnlk")
#model = project.version(3).model
TextColor = (255, 255, 255)
outlineColor = (0, 0, 0)  # RGB color for black
DEPLOYMENT = False # !!! REMEMBER TO CHANGE for deployment !!!
text_size=1
text_thickness=1
app = flask.Flask(__name__)
app.secret_key = os.urandom(8)
user_id=""
access_token=""
if not DEPLOYMENT:
    CORS(app)

def base64_to_image(base64_data, output_filename):
    try:
        decoded_img_data = base64.b64decode(base64_data)
        with open(output_filename, 'wb') as img_file:
            img_file.write(decoded_img_data)
        print(f"Image saved as {output_filename}")
    except Exception as e:
        print(f"Error decoding base64 image: {str(e)}")

@app.route('/api/user', methods=['POST'])
def handle_user_input():

    input_data = request.get_json()
    print(input_data)
    if not input_data:
        # If there's no data, or it's not JSON, return an error
        return flask.jsonify({'error': 'No data provided'}), 400

    # Assuming the key for the input data is 'username', adjust as necessary
    username = input_data.get('username')
    if not username:
        # If the expected key isn't found in the JSON, return an error
        return flask.jsonify({'error': 'Missing username'}), 400

    print(f"Received username: {username}")
    resultSmoker=""
    if username=="test1":
        resultSmoker=smokerALgo("test1")
    elif(username=="test2"):
        resultSmoker=smokerALgo("test2")
    else:
        resultSmoker=smokerALgo("test3")
    counter=0
    tempList=[]
    for data in resultSmoker[0]:
        print(data)
        file_name = data[len(data)-1]
        if not os.path.isfile(file_name):
            print(f"File does not exist: {file_name}")
            continue
        image=cv2.imread(file_name)
        if(data[len(data)-2]==1 or data[len(data)-2]==1):
            center=data[1]
            radius=data[2]
            color = (0, 0, 0)  # RGB color of the circle
            thickness = 2  # Thickness of the circle outline, in pixels
            image = cv2.circle(image, center, radius, color, thickness)
            center=data[3]
            radius=data[4]
            image = cv2.circle(image, center, radius, color, thickness)
        elif(data[len(data)-2]==3):
            center=data[1]
            radius=data[2]
            color = (0, 255, 0)  # RGB color of the circle
            thickness = 2  # Thickness of the circle outline, in pixels
            image = cv2.circle(image, center, radius, color, thickness)
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer).decode()
        print("done")
        tempList.append(jpg_as_text)

    return flask.jsonify({'message': 'Username received successfully', 'images':json.dumps(tempList), 'info':json.dumps(resultSmoker)}), 200


# After user agrees (on Instagram) to give us access, Instagram redirects them to this endpoint.
# This endpoint obtains the user's id and the access token, stores them in the Flask session and
# redirects them to the /instagram page.
@app.route('/api/instagram-redirect')
def instagram_redirect():
    global user_id, access_token
    localuser_id, localaccess_token = instagram_api.get_credentials(code=request.args['code'], server=DEPLOYMENT)
    user_id=localuser_id
    access_token=localaccess_token
    return flask.redirect('/instagram' if DEPLOYMENT else 'http://localhost:3000/instagram')


# Our Instagram Analysis sends a request to this endpoint to download user's images and comments,
# analyse them and return the result of that analysis.
# TODO: Actually analyse them and return the result of the analysis.
@app.route('/api/instagram-analysis')
def instagram_analysis():
    global text_size, text_thickness, TextColor, outlineColor
    try:
        instagram_api.download_media(user_id, access_token, 'downloads')
    except Exception as e:
        return flask.jsonify({'success': False})
    resultSmoker=smokerALgo("downloads")
    tempList=[]

    u_name = instagram_api.get_username(user_id, access_token)

    for data in resultSmoker[0]:
        print(data)
        file_name = data[len(data)-1]
        if not os.path.isfile(file_name):
            print(f"File does not exist: {file_name}")
            continue
        image=cv2.imread(file_name)
        if(data[len(data)-2]==1 ):
            center=data[1]
            radius=data[2]
            color = (0, 0, 255)  # RGB color of the circle
            cThickness = 2  # Thickness of the circle outline, in pixels
            image = cv2.circle(image, center, radius, color, cThickness)
            font = cv2.FONT_HERSHEY_SIMPLEX
            center_text = (center[0], center[1] - int(radius/2))
            image = cv2.putText(image, 'Cigarette', center_text, font, text_size, outlineColor, text_thickness + 2, cv2.LINE_AA)
            image = cv2.putText(image, 'Cigarette', center_text, font, text_size, TextColor, text_thickness, cv2.LINE_AA)

            center=data[3]
            radius=data[4]
            color = (0, 255, 0)  # RGB color of the circle

            image = cv2.circle(image, center, radius, color, cThickness)
            center_text = (center[0], center[1] - int(radius/2))
            image = cv2.putText(image, 'Face', center_text, font, text_size, outlineColor, text_thickness + 2, cv2.LINE_AA)
            image = cv2.putText(image, 'Face', center_text, font, text_size, TextColor, text_thickness, cv2.LINE_AA)

        elif(data[len(data)-2]==2):
            center=data[1]
            radius=data[2]
            color = (0, 0, 255)  # RGB color of the circle
            cThickness = 2  # Thickness of the circle outline, in pixels
            image = cv2.circle(image, center, radius, color, cThickness)
            font = cv2.FONT_HERSHEY_SIMPLEX
            center_text = (center[0], center[1] - int(radius/2))
            image = cv2.putText(image, 'Cigarette', center_text, font, text_size, outlineColor, text_thickness + 2, cv2.LINE_AA)
            image = cv2.putText(image, 'Cigarette', center_text, font, text_size, TextColor, text_thickness, cv2.LINE_AA)
            center=data[3]
            radius=data[4]
            color = (255, 0, 0)  # RGB color of the circle
            image = cv2.circle(image, center, radius, color, cThickness)
            center_text = (center[0], center[1] - int(radius/2))
            image = cv2.putText(image, 'Hand', center_text, font, text_size, outlineColor, text_thickness + 2, cv2.LINE_AA)
            image = cv2.putText(image, 'Hand', center_text, font, text_size, TextColor, text_thickness, cv2.LINE_AA)

        elif(data[len(data)-2]==3):
            center=data[1]
            radius=data[2]
            color = (0, 0, 255)  # RGB color of the circle
            cThickness = 2  # Thickness of the circle outline, in pixels
            image = cv2.circle(image, center, radius, color, cThickness)
            font = cv2.FONT_HERSHEY_SIMPLEX
            center_text = (center[0], center[1] - int(radius/2))
            image = cv2.putText(image, 'Cigarette', center_text, font, text_size, outlineColor, text_thickness + 2, cv2.LINE_AA)
            image = cv2.putText(image, 'Cigarette', center_text, font, text_size, TextColor, text_thickness, cv2.LINE_AA)
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer).decode()
        print("done")
        tempList.append(jpg_as_text)

    return flask.jsonify({'message': 'Username received successfully', 'images':json.dumps(tempList), 'info':json.dumps(resultSmoker), 'username':u_name}), 200
    # TODO: Analyse the images
    # TODO: Analyse the comments
    # TODO: Prepare a response for the front-end


#@app.route('/api/upload', methods=['POST'])
#def upload_image():
#    todo_data = request.get_json()
#    base64_to_image(todo_data['lmao'], 'output.jpg')
#    answer=model.predict("output.jpg", confidence=40, overlap=30).json()
#    model.predict("output.jpg", confidence=30, overlap=30).save("answer.jpg")
#    with open("answer.jpg", "rb") as image_file:
#        encoded_string = base64.b64encode(image_file.read()).decode()
#    with open('encoded_string.txt', 'w') as file:
#        file.write(encoded_string)
#    print('sending reply all done')
#    return flask.jsonify({'data':answer,'image':encoded_string}),201

def test_build():
    try:
        app.test_client().get('/')
        print("Build successful.")
        return True
    except Exception as e:
        print(f"Build failed: {str(e)}")
        return False

#epic comment
#also epic comment
#this is an epic comment
def epic_comment():
    print("epic comment")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--build-test', action='store_true')
    args = parser.parse_args()

    if args.build_test:
        if test_build():
            exit(0)
        else:
            exit(1)
    else:
        app.run(debug=True, ssl_context=('server.crt', 'server.key'))
