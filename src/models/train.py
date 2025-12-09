from src.data.data_loader import load_synthetic_data
from src.features.preprocessing import prepare_features
from src.models.barrier_model import BarrierModel

DATA_PATH = "synthetic_data/synthetics_furniture_barriers.csv"
MODEL_PATH = "models/barrier_model.joblib"

def main():
    df = load_synthetic_data(DATA_PATH)

    X, y, _ = prepare_features(df)

    model = BarrierModel()
    model.fit(X, y)
    model.save(MODEL_PATH)

    print("Model trained and saved")

if __name__ == "__main__":
    main()