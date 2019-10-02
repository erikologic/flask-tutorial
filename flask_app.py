# flask_app.py
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World!"



@app.route("/api")
def get_data():
    data = pd.DataFrame({
        'keys': ['a', 'b', 'c'],
        'values': [1, 2, 3]
    })
    return jsonify(data.to_dict(orient="records"))

@app.route("/api", methods=["POST"])
def post_data():
    data = pd.DataFrame(request.get_json())
    return jsonify(data.to_dict(orient="records"))
