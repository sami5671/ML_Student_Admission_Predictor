import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load dataset from CSV
df = pd.read_csv("dataset.csv")

# Separate features and target
X = df[["GRE Score", "TOEFL Score", "CGPA", "Research"]]
y = df["Admitted"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
