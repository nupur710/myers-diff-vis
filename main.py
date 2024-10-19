from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from myers import myers_diff

app= Flask(__name__)
CORS(app)

@app.route('/api/diff', methods=["POST"])
def calculate_diff():
    data = request.json
    src_string = data['string1']
    dest_string = data['string2']
    result = myers_diff(src_string, dest_string)

    return jsonify(result)

@app.route('/')
def display_frontend():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)