import pandas as pd
import os

BASE_PATH = "data/datasets"

def load_dataset(file_name):
    path = os.path.join(
        BASE_PATH,
        file_name
    )
    return pd.read_csv(path)
