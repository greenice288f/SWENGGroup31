import argparse
from flask import Flask, jsonify,request
from flask_cors import CORS  # Comment out for deployment
from PIL import Image
import base64
from roboflow import Roboflow
import cv2
import text_analysis

rf = Roboflow(api_key="Tao36WXLMwnYXJt3uFaj")
project = rf.workspace("cigarette-c6554").project("cigarette-ghnlk")
model = project.version(3).model
app = Flask(__name__)
CORS(app)  # Comment out for deployment

def base64_to_image(base64_data, output_filename):
    try:
        decoded_img_data = base64.b64decode(base64_data)
        with open(output_filename, 'wb') as img_file:
            img_file.write(decoded_img_data)
        print(f"Image saved as {output_filename}")
    except Exception as e:
        print(f"Error decoding base64 image: {str(e)}")

@app.route('/user', methods=['POST'])
def handle_user_input():
    # Attempt to get JSON data from the request
    input_data = request.get_json()
    if not input_data:
        # If there's no data, or it's not JSON, return an error
        return jsonify({'error': 'No data provided'}), 400

    # Assuming the key for the input data is 'username', adjust as necessary
    username = input_data.get('username')
    if not username:
        # If the expected key isn't found in the JSON, return an error
        return jsonify({'error': 'Missing username'}), 400

    print(f"Received username: {username}")
    
    # Here, add your logic to process the username, such as querying a database,
    # calling an external API, or any other processing based on your application's needs.

    # Return a response to indicate success
    return jsonify({'message': 'Username received successfully', 'username': username}), 200


@app.route('/upload', methods=['POST'])
def upload_image():
    todo_data = request.get_json()
    base64_to_image(todo_data['lmao'], 'output.jpg')
    answer=model.predict("output.jpg", confidence=40, overlap=30).json()
    model.predict("output.jpg", confidence=30, overlap=30).save("answer.jpg")
    with open("answer.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    with open('encoded_string.txt', 'w') as file:
        file.write(encoded_string)
    print('sending reply all done')
    return jsonify({'data':answer,'image':encoded_string}),201

@app.route('/analyze', methods=['POST'])
def analyze_text():
    input_data = request.get_json()
    if not input_data:
        return jsonify({'error': 'No data provided'}), 400
    comments = input_data['comments']
    if not comments:
        return jsonify({'analysis_results': 'No comments provided'}),201
    return jsonify({'analysis_results': text_analysis(comments)}),201


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
        app.run(debug=True)