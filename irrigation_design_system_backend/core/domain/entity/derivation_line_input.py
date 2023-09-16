from decimal import Decimal
from dataclasses import dataclass


@dataclass
class DerivationLineDiameterInput:
    demand_flow: Decimal
    speed_max: Decimal


@dataclass
class DerivationLineLoadLossInput:
    length_derivation_line: Decimal
    flow: Decimal
    n_outputs: Decimal
    diameter_derivation_line: Decimal
