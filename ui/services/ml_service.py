from src.models.predict import predict

def classify_users(csv_path, model_path):
    return predict(csv_path, model_path)
