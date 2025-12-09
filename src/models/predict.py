from src.models.barrier_model import BarrierModel
from src.features.preprocessing import prepare_features
from src.data.data_loader import load_synthetic_data

def predict(data_path, model_path):
    df = load_synthetic_data(data_path)
    X, _, _ = prepare_features(df)

    model = BarrierModel.load(model_path)
    df["predicted_barrier"] = model.predict(X)

    return df