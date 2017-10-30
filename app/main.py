from flask import Flask,jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.6 (from the example template)"

@app.route("/ping")
def ping():
    return jsonify({'response:': 'Pong'})


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
