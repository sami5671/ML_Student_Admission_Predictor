import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Sample fake dataset
data = {
    "GRE Score": [320, 300, 310, 315, 305],
    "TOEFL Score": [110, 100, 105, 107, 102],
    "CGPA": [8.6, 7.5, 8.0, 8.3, 7.9],
    "Research": [1, 0, 1, 1, 0],
    "Admitted": [1, 0, 1, 1, 0],
}

df = pd.DataFrame(data)

X = df[["GRE Score", "TOEFL Score", "CGPA", "Research"]]
y = df["Admitted"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
