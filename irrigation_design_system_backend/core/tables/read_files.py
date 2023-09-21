import pandas as pd


def read_file(path: str, delimiter: str = ";"):
    data = pd.read_csv(path, delimiter=delimiter, decimal=",", encoding="utf-8").interpolate(
        method="values", axis=1, limit_direction="both", limit=1
    )
    return data
