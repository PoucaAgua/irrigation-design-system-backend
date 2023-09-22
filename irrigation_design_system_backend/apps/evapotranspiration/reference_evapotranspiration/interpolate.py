import pandas as pd
from scipy.interpolate import interp1d


def interpolate(x: pd.Series, y: pd.Series, value: float) -> float:
    interp_func = interp1d(x, y, kind="linear", fill_value="extrapolate")
    return interp_func(value).tolist()
