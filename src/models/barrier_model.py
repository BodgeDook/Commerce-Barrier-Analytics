import joblib
from xgboost import XGBClassifier

class BarrierModel:
    def __init__(self):
        self.model = XGBClassifier(
            n_estimators=100,
            max_depth=5,
            learning_rate=0.1,
            eval_metric="mlogloss",
            random_state=42
        )

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def save(self, path: str):
        joblib.dump(self.model, path)

    @staticmethod
    def load(path: str):
        instance = BarrierModel()
        instance.model = joblib.load(path)
        return instance