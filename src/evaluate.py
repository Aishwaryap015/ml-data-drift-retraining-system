import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

def evaluate_model(data_path):
    df = pd.read_csv(data_path)

    X = df.drop("target", axis=1)
    y = df["target"]

    model = joblib.load("models/model.pkl")
    preds = model.predict(X)

    acc = accuracy_score(y, preds)
    return acc