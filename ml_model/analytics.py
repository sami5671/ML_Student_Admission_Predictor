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

    # Plot bar chart
    plt.figure(figsize=(8, 6))
    sns.barplot(x=feature_importance, y=feature_names, palette="viridis")
    plt.title("Feature Importance (Bar Chart)")
    plt.xlabel("Coefficient Value")
    plt.tight_layout()
    plt.savefig("static/feature_importance_bar.png")
    plt.close()

    # Plot heatmap of correlation matrix
    plt.figure(figsize=(8, 6))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("static/feature_correlation_heatmap.png")
    plt.close()

    return {
        "bar_chart": "/static/feature_importance_bar.png",
        "heatmap": "/static/feature_correlation_heatmap.png",
    }
