from src.train import train_model
from src.detect_drift import detect_drift
from src.retrain import retrain
from src.evaluate import evaluate_model
from src.logger import log

def main():
    print("\n🚀 Starting Smart Data Drift Pipeline...\n")

    # Train initial model
    train_model()
    acc_before = evaluate_model("data/train.csv")
    print(f"📊 Initial Accuracy: {acc_before:.2f}")
    log(f"Initial Accuracy: {acc_before}")

    # Detect drift
    drift = detect_drift()

    if drift:
        print("\n⚠️ Drift detected! Retraining model...")
        log("Drift detected")

        retrain()

        acc_after = evaluate_model("data/new_data.csv")
        print(f"📊 Accuracy After Retrain: {acc_after:.2f}")
        log(f"Accuracy after retrain: {acc_after}")

    else:
        print("\n✅ No drift detected. Model is stable.")
        log("No drift detected")

    print("\n✅ Pipeline completed successfully!")

if __name__ == "__main__":
    main()