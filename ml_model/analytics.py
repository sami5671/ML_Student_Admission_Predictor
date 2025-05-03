# analytics.py
import os
import pickle

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

os.makedirs("static", exist_ok=True)


def generate_feature_contribution_graphs():
    # Load dataset
    df = pd.read_csv("dataset.csv")
    X = df[["GRE Score", "TOEFL Score", "CGPA", "Research"]]

    # Load model
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    # Get feature names and coefficients
    feature_names = X.columns
    feature_importance = model.coef_[0]

    # Plot bar chart (Feature Importance)
    plt.figure(figsize=(8, 6))
    sns.barplot(x=feature_importance, y=feature_names, palette="viridis")
    plt.title("Feature Importance (Bar Chart)")
    plt.xlabel("Coefficient Value")
    plt.tight_layout()
    plt.savefig("static/feature_importance_bar.png")
    plt.close()

    # Plot box plots for each feature vs Admission
    features = ["GRE Score", "TOEFL Score", "CGPA", "Research"]
    for feature in features:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x="Admitted", y=feature, data=df, palette="pastel")
        plt.title(f"{feature} by Admission Status")
        plt.xlabel("Admitted (0 = No, 1 = Yes)")
        plt.ylabel(feature)
        plt.tight_layout()
        filename = f"static/{feature.replace(' ', '_').lower()}_boxplot.png"
        plt.savefig(filename)
        plt.close()

    return {
        "bar_chart": "/static/feature_importance_bar.png",
        "boxplots": {
            feature: f"/static/{feature.replace(' ', '_').lower()}_boxplot.png"
            for feature in features
        },
    }
