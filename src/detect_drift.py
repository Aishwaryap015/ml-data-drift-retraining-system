import pandas as pd
from scipy.stats import ks_2samp
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

def detect_drift(threshold=0.05):
    train = pd.read_csv("data/train.csv")
    new_data = pd.read_csv("data/new_data.csv")

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=train, current_data=new_data)
    report.save_html("reports/drift_report.html")

    drift_count = 0
    total_features = len(train.columns) - 1  # exclude target

    for col in train.columns:
        if col == "target":
            continue

        stat, p_value = ks_2samp(train[col], new_data[col])

        if p_value < threshold:
            drift_count += 1

    drift_ratio = drift_count / total_features

    print(f"🔍 Drift Ratio: {drift_ratio:.2f}")

    # If more than 50% features drifted → trigger retrain
    if drift_ratio > 0.5:
        print("⚠️ Significant drift detected!")
        return True
    else:
        print("✅ No significant drift.")
        return False