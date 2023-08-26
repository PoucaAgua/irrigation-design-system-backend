from _decimal import Decimal

class LateralLineConstants:
  kinematic_viscosity = Decimal(0.00000101) # m²/s
  
class FrictorFactorConstants:
  transition_factor = Decimal(0.04)
  m = Decimal(0.25)
  c = Decimal(0.316)
