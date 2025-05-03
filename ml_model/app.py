# import os
# import pickle

# import matplotlib.pyplot as plt
# import numpy as np
# from analytics import generate_feature_contribution_graphs
# from flask import Flask, jsonify, request, send_file
# from flask_cors import CORS

# app = Flask(__name__)
# os.makedirs("static", exist_ok=True)
# CORS(app)

# model = pickle.load(open("model.pkl", "rb"))


# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()

#     # Convert input to correct numeric types
#     gre = float(data["gre"])
#     toefl = float(data["toefl"])
#     cgpa = float(data["cgpa"])
#     research = int(data["research"])

#     # Prepare input for model
#     input_features = np.array([[gre, toefl, cgpa, research]])
#     prob = model.predict_proba(input_features)[0][1] * 100

#     # Coefficients and normalization
#     coefs = model.coef_[0]
#     feature_names = ["GRE Score", "TOEFL Score", "CGPA", "Research"]
#     user_values = [gre, toefl, cgpa, research]
#     max_values = [340, 120, 4.0, 1]  # Max values for normalization

#     normalized = [val / max_v for val, max_v in zip(user_values, max_values)]
#     contributions = [coef * norm for coef, norm in zip(coefs, normalized)]

#     # Create feature contribution graph
#     plt.figure(figsize=(8, 5))
#     plt.barh(feature_names, contributions, color="orange")
#     plt.xlabel("Contribution Score")
#     plt.title("Your Feature Impact on Admission Prediction")
#     plt.tight_layout()
#     image_path = "static/feature_contribution_user.png"
#     plt.savefig(image_path)
#     plt.close()

#     # Generate smart recommendations
#     recommendations = []
#     threshold = 0.8  # Feature score threshold

#     for norm, coef, name in zip(normalized, coefs, feature_names):
#         if norm < threshold and coef > 0:
#             if name == "Research":
#                 recommendations.append(
#                     "Having research experience can significantly improve your chances. Try to participate in one."
#                 )
#             else:
#                 recommendations.append(
#                     f"Your {name} is relatively low. Improving it may increase your chances of admission."
#                 )

#     return jsonify(
#         {
#             "admission_chance": round(prob, 2),
#             "suggestion_graph": "/static/feature_contribution_user.png",
#             "recommendations": recommendations,
#         }
#     )


# @app.route("/analytics/feature-importance")
# def feature_importance():
#     result = generate_feature_contribution_graphs()
#     return jsonify(result)


# if __name__ == "__main__":
#     app.run(port=5000)


import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
from analytics import generate_feature_contribution_graphs
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
os.makedirs("static", exist_ok=True)
CORS(app)

# Load your trained model
model = pickle.load(open("model.pkl", "rb"))


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Convert input to correct numeric types
    gre = float(data["gre"])
    toefl = float(data["toefl"])
    cgpa = float(data["cgpa"])
    research = int(data["research"])

    # Prepare input for model
    input_features = np.array([[gre, toefl, cgpa, research]])
    prob = model.predict_proba(input_features)[0][1] * 100

    # Coefficients and normalization
    coefs = model.coef_[0]
    feature_names = ["GRE Score", "TOEFL Score", "CGPA", "Research"]
    user_values = [gre, toefl, cgpa, research]
    max_values = [340, 120, 4.0, 1]  # Max values for normalization

    normalized = [val / max_v for val, max_v in zip(user_values, max_values)]

    # Generate improvement recommendation graph
    improvable_features = []
    improvement_gaps = []

    for norm, coef, name in zip(normalized, coefs, feature_names):
        if norm < 0.95 and coef > 0:
            improvable_features.append(name)
            improvement_gaps.append(1.0 - norm)

    plt.figure(figsize=(8, 5))
    plt.barh(improvable_features, improvement_gaps, color="skyblue")
    plt.xlabel("Improvement Needed (towards max value)")
    plt.title("Features to Improve for Better Admission Chances")
    plt.tight_layout()
    image_path = "static/feature_improvement_graph.png"
    plt.savefig(image_path)
    plt.close()

    # Generate recommendations
    recommendations = []
    for norm, coef, name in zip(normalized, coefs, feature_names):
        if norm < 0.8 and coef > 0:
            if name == "Research":
                recommendations.append(
                    "Having research experience can significantly improve your chances. Try to participate in one."
                )
            else:
                recommendations.append(
                    f"Your {name} is relatively low. Improving it may increase your chances of admission."
                )

    return jsonify(
        {
            "admission_chance": round(prob, 2),
            "improvement_graph": "/static/feature_improvement_graph.png",
            "recommendations": recommendations,
        }
    )


@app.route("/analytics/feature-importance")
def feature_importance():
    result = generate_feature_contribution_graphs()
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000)
