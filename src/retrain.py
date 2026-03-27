import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def retrain():
    df = pd.read_csv("data/new_data.csv")

    X = df.drop("target", axis=1)
    y = df["target"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "models/model.pkl")
    print("🔁 Model retrained with new data!")

if __name__ == "__main__":
    retrain()