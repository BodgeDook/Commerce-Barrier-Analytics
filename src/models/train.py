import joblib

from data.data_loader import load_synthetic_data
from src.features.preprocessing import fit_transform_features
from src.models.barrier_model import BarrierModel

DATA_PATH = "synthetic_data/synthetics_furniture_barriers.csv"
MODEL_PATH = "models/barrier_model.joblib"
PREPROCESSOR_PATH = "models/preprocessor.joblib"

def main():
    df = load_synthetic_data(DATA_PATH)

    X, y, preprocessor = fit_transform_features(df)

    model = BarrierModel()
    model.fit(X, y)

    model.save(MODEL_PATH)
    joblib.dump(preprocessor, PREPROCESSOR_PATH)

    print("Model and preprocessor saved successfully")

if __name__ == "__main__":
    main()