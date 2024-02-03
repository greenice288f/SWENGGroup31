from flask import Flask, jsonify
from flask_cors import CORS  # Comment out for deployment

app = Flask(__name__)
CORS(app)  # Comment out for deployment

@app.route('/sokaigeljenorbitron')
def hello_world():
    data = {
        'message': 'Hello from server'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
