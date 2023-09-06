from decimal import Decimal
from dataclasses import dataclass

@dataclass
class DerivationlineDiameterEntity:
  
  demand_flow:              Decimal
  speed_max:                Decimal 

@dataclass
class DerivationlineLoadLoassEntity:
  
  length_derivationline:    Decimal
  flow:                     Decimal
  n_outputs:                Decimal
  line_spacing:             Decimal
  diameter_derivationline:  Decimal
