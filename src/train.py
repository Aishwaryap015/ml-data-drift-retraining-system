import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    df = pd.read_csv("data/train.csv")

    X = df.drop("target", axis=1)
    y = df["target"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "models/model.pkl")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_model()