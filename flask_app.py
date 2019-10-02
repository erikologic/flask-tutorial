# flask_app.py
from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World!"

data = {"a": 1, "b": 2}
@app.route("/api")
def my_api():
    return jsonify(data)

