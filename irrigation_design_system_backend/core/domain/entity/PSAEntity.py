from _decimal import Decimal
from dataclasses import dataclass

@dataclass
class SAEntity:

    strip_shaded_by_the_plant: Decimal 
    diameter_of_the_plants_canopy_projection: Decimal 
    space_between_plants: Decimal 

@dataclass
class CPEntity:

    strip_shaded_by_the_plant: Decimal 
    shaded_strip_plant: Decimal 