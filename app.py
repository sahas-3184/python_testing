from flask import Flask, request, jsonify

# Flask App Definition
app = Flask(__name__)

@app.route('/api/test', methods=['GET', 'POST'])
def test_endpoint():
    if request.method == 'GET':
        return jsonify({"message": "This is a GET request", "params": request.args}), 200
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Unsupported Media Type"}), 415
        return jsonify({"message": "This is a POST request", "data": request.json}), 201

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True)
