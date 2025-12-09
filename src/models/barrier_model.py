import joblib
from xgboost import XGBClassifier

class BarrierModel:
    def __init__(self):
        self.model = XGBClassifier(
            n_estimators=100,
            max_depth=5,
            learning_rate=0.1,
            eval_metric="mlogloss"
        )

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path: str):
        joblib.dump(self.model, path)

    @staticmethod
    def load(path: str):
        model = BarrierModel()
        model.model = joblib.load(path)
        return model