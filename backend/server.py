import argparse
from flask import request
import flask
from flask_cors import CORS
import base64
import json
from smokerAlgo import smokerALgo
import os
import instagram_api

#rf = Roboflow(api_key="Tao36WXLMwnYXJt3uFaj")
#project = rf.workspace("cigarette-c6554").project("cigarette-ghnlk")
#model = project.version(3).model

DEPLOYMENT = False # !!! REMEMBER TO CHANGE for deployment !!!

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
        encoded_string = ""
        with open(file_name, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        tempList.append(encoded_string)

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
    try:
        instagram_api.download_media(user_id, access_token, 'downloads')
    except Exception as e:
        return flask.jsonify({'success': False})
    resultSmoker=smokerALgo("downloads")
    tempList=[]
    for data in resultSmoker[0]:
        print(data)
        file_name = data[len(data)-1]
        if not os.path.isfile(file_name):
            print(f"File does not exist: {file_name}")
            continue
        encoded_string = ""
        with open(file_name, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        tempList.append(encoded_string)

    return flask.jsonify({'message': 'Username received successfully', 'images':json.dumps(tempList), 'info':json.dumps(resultSmoker)}), 200
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