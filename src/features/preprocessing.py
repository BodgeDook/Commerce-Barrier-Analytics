import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

TEXT_COL = "x9_chat_text"
TARGET = "Barrier_Class"

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
    "x10_reviews"
]

def prepare_features(df: pd.DataFrame):
    df = df.copy()

    df[TEXT_COL] = df[TEXT_COL].fillna("")

    X_num = df[NUM_COLS]
    y = df[TARGET]

    vectorizer = TfidfVectorizer(max_features=50)
    X_text = vectorizer.fit_transform(df[TEXT_COL])

    X = pd.concat(
        [X_num.reset_index(drop=True),
         pd.DataFrame(X_text.toarray())],
        axis=1
    )

    return X, y, vectorizer