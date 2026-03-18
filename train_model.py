import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("dataset.csv")

X = data[["hours"]]
y = data["pass"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully!")