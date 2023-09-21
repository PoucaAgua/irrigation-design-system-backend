from _decimal import Decimal
import pandas as pd
from scipy.interpolate import interp1d

def calculate_temperature_media(temperature_media: Decimal, temperature_max: Decimal, temperature_min: Decimal, days: Decimal):
    if temperature_media is not None:
        return temperature_media

    if temperature_max is not None and temperature_min is not None and days is not None and days != 0:
        calculated_temperature_media = (temperature_max / days + temperature_min / days) / 2
        return calculated_temperature_media
   

def interpolate(x: pd.Series, y: pd.Series, value: float):
    interp_func = interp1d(x, y, kind='linear', fill_value="extrapolate")
    return interp_func(value)


