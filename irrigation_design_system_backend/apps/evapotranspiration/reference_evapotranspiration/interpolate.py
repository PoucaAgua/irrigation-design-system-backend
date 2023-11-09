import pandas as pd
import numpy as np


def interpolate(x: pd.Series, y: pd.Series, value: float) -> float:
    sorted_idx = x.argsort()
    x = x[sorted_idx]
    y = y[sorted_idx]

    idx = np.searchsorted(x, value)
    if idx == 0:
        slope = (y.iloc[1] - y.iloc[0]) / (x.iloc[1] - x.iloc[0])
        return y.iloc[0] + slope * (value - x.iloc[0])
    elif idx == len(x):
        slope = (y.iloc[-1] - y.iloc[-2]) / (x.iloc[-1] - x.iloc[-2])
        return y.iloc[-1] + slope * (value - x.iloc[-1])
    else:
        x1, x2 = x.iloc[idx - 1], x.iloc[idx]
        y1, y2 = y.iloc[idx - 1], y.iloc[idx]
        slope = (y2 - y1) / (x2 - x1)
        return y1 + slope * (value - x1)
