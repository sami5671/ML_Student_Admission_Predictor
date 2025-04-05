import os
import pickle

import numpy as np
from analytics import generate_feature_contribution_graphs
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    print(data)
    features = np.array(
        [
            float(data["gre"]),
            float(data["toefl"]),
            float(data["cgpa"]),
            int(data["research"]),
        ]
    ).reshape(1, -1)

    prediction = model.predict(features)[0]
    return jsonify({"admission": bool(prediction)})


@app.route("/analytics/feature-importance")
def feature_importance():
    result = generate_feature_contribution_graphs()
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000)
