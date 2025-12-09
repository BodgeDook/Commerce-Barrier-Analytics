import pandas as pd
from pathlib import Path

def load_synthetic_data(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)