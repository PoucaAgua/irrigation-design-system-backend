from decimal import Decimal
from dataclasses import dataclass


@dataclass
class DummyEntity:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    radiation: Decimal
