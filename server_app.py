from flask import Flask, request, jsonify, gunicorn

app = Flask(__name__)

# Define a simple GET API
@app.route('/hello')
def hello():
    return 'Hello, World!'

# Define a POST API that accepts JSON data
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    # Do something with the data, e.g. save it to a database
    response = {'message': 'Data received successfully'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
