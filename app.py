from flask import Flask,jsonify,request


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello my little friends'

app.run(host="0.0.0.0", port=8080)