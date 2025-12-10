import joblib
import pandas as pd

from src.features.preprocessing import transform_features
from src.models.barrier_model import BarrierModel

MODEL_PATH = "models/barrier_model.joblib"
PREPROCESSOR_PATH = "models/preprocessor.joblib"

def predict(df: pd.DataFrame):
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    model = BarrierModel.load(MODEL_PATH)

    X = transform_features(df, preprocessor)

    preds = model.predict(X)
    probs = model.predict_proba(X)

    return preds, probs