from decimal import Decimal
from dataclasses import dataclass

@dataclass
class LateralLineEntity:
  pass

@dataclass
class ReynoldsNumber:
  flow_velocity: Decimal
  pipe_diameter: Decimal