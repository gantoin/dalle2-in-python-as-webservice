from flask import Flask, jsonify, request
from flask_cors import CORS

from dalle2 import Dalle2

app = Flask(__name__)
CORS(app)


@app.route('/generate', methods=['POST'])
def generate():
    content_type = request.headers['Content-Type']
    if content_type == 'application/json':
        data = request.get_json().get('prompt')
        dalle = Dalle2("XXXX")
        generations = dalle.generate(data)
        return jsonify(generations)
    else:
        return jsonify({'error': 'Content-Type must be application/json'}), 400


if __name__ == '__main__':
    app.run(debug=True)
