from flask import Flask, jsonify,request
from flask_cors import CORS  # Comment out for deployment
from PIL import Image
import base64
from roboflow import Roboflow
import cv2
import base64

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

@app.route('/xd')
def asd():
    #print(model.predict("155135c1-7f8d-49b3-9a91-2db7572842ae.jpg", confidence=40, overlap=30).json())
    data = {
        'message': 'Hello from server'
    }
    return jsonify(data)


@app.route('/sokaigeljenorbitron')
def hello_world():
    data = {
        'message': 'Hello from server'
    }
    return jsonify(data)


@app.route('/upload', methods=['POST'])
def upload_image():
    todo_data = request.get_json()
    print(type(todo_data['lmao']))
    base64_to_image(todo_data['lmao'], 'output.jpg')
    answer=model.predict("output.jpg", confidence=40, overlap=30).json()

    return jsonify(answer),201
if __name__ == '__main__':
    app.run(debug=True)
