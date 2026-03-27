import pandas as pd
import numpy as np

np.random.seed(42)

train = pd.DataFrame({
    "feature1": np.random.normal(50, 10, 500),
    "feature2": np.random.normal(30, 5, 500),
    "target": np.random.randint(0, 2, 500)
})

# Drift introduced here
new_data = pd.DataFrame({
    "feature1": np.random.normal(70, 15, 200),
    "feature2": np.random.normal(20, 10, 200),
    "target": np.random.randint(0, 2, 200)
})

train.to_csv("data/train.csv", index=False)
new_data.to_csv("data/new_data.csv", index=False)

print("✅ Data generated successfully!")