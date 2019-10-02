# flask_app.py
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World!"


data = pd.DataFrame({
    'keys': ['a', 'b', 'c'],
    'values': [1, 2, 3]
})
@app.route("/api")
def my_api():
    return jsonify(data.to_dict(orient="records"))

