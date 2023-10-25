from decimal import Decimal
from typing import Optional


def calculate_temperature_med(
    temperature_med: Optional[Decimal] = None,
    temperature_max: Optional[Decimal] = None,
    temperature_min: Optional[Decimal] = None,
    **kwargs
):
    if temperature_med is not None:
        return temperature_med

    if temperature_max is not None and temperature_min is not None:
        return (temperature_max + temperature_min) / 2

    raise ValueError(
        "Needs to have temperature_med or both temperature_max and temperature_min"
    )
