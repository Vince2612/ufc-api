from flask import Flask, jsonify
from ufc import get_upcoming_events

app = Flask(__name__)

@app.route('/get_upcoming_events')
def get_upcoming():
    return get_upcoming_events()

@app.route("/hello", methods=["GET"])
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'



if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5060, debug=True)

