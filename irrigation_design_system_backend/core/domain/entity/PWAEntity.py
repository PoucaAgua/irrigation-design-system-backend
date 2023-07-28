from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class PWAEntity:
    drippers_number: int
    max_diameter: Decimal
    space_between_lines: Decimal
    space_between_plants: Decimal
