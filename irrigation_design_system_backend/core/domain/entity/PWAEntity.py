from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class IBTEntity:
    
    drippers_number: int 
    space_between_lines: Decimal 
    space_between_plants: Decimal 

    value_of_z: Decimal 
    value_of_q: Decimal 
    hydraulic_conductivity_of_saturated_soil: Decimal 


@dataclass
class TSWEntity:

    space_between_plants: Decimal 
    wetted_zone: Decimal 
    row_spacing_plants: Decimal 

 
@dataclass
class CPEntity:
  
    parameter_model_unsaturated_hydraulic: Decimal 
    hydraulic_conductivity_of_saturated_soil: Decimal 
    value_of_q: Decimal 