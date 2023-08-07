from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class PlantCanopyProjectionInputEntity:
    diameter_projection: Decimal
    space_between_plants: Decimal
    space_between_rows: Decimal


@dataclass
class PlantStripProjectionInputEntity:
    space_between_rows: Decimal
    shaded_strip_plant: Decimal
