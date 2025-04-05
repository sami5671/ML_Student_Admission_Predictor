import pickle

import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(
        [data["gre"], data["toefl"], data["cgpa"], data["research"]]
    ).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"admission": bool(prediction)})


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Admission Predictor API"})


if __name__ == "__main__":
    app.run(port=5000)
