import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler
from sklearn.feature_extraction.text import TfidfVectorizer

TEXT_COL = "x9_chat_text"
TARGET_COL = "Barrier_Class"

NUM_COLS = [
    "x1_views",
    "x2_chars_pdf",
    "x3_ship_page",
    "x4_calc_used",
    "x4_ship_cost",
    "x5_assembly_page",
    "x6_warranty",
    "x7_return_page",
    "x8_email_clicks",
    "x10_reviews",
]

def build_preprocessor() -> ColumnTransformer:
    numeric_pipeline = Pipeline(
        steps=[
            ("scaler", RobustScaler())
        ]
    )

    text_pipeline = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    max_features=50,
                    ngram_range=(1, 2),
                    stop_words="russian",
                )
            )
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, NUM_COLS),
            ("text", text_pipeline, TEXT_COL),
        ],
        remainder="drop"
    )

    return preprocessor

def fit_transform_features(df: pd.DataFrame):
    df = df.copy()
    df[TEXT_COL] = df[TEXT_COL].fillna("")

    X = df[NUM_COLS + [TEXT_COL]]
    y = df[TARGET_COL]

    preprocessor = build_preprocessor()
    X_transformed = preprocessor.fit_transform(X)

    return X_transformed, y, preprocessor

def transform_features(df: pd.DataFrame, preprocessor: ColumnTransformer):
    df = df.copy()
    df[TEXT_COL] = df[TEXT_COL].fillna("")

    X = df[NUM_COLS + [TEXT_COL]]
    X_transformed = preprocessor.transform(X)

    return X_transformed