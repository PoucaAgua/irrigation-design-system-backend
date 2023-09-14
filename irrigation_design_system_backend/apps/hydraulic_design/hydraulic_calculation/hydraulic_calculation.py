from _decimal import Decimal
from core.constants.hydraulic_design import HydraulicConstants
from core.constants.math import MathConstants

class HydraulicCalculation:

  @staticmethod
  def n_outputs():
    return HydraulicConstants.length_derivationline / HydraulicConstants.line_spacing

  @staticmethod
  def speed_water(q, d) -> Decimal:

    pi = MathConstants.PI

    speed = Decimal(4*q) / ((Decimal(d)**2) * pi)

    return speed

  @staticmethod
  def n_reynolds(speed, diameter) -> Decimal:

    visc = HydraulicConstants.kinematic_viscosity

    num_reynolds = Decimal(diameter * speed) / visc

    return num_reynolds

  @staticmethod
  def friction_factor(d, re) -> Decimal:

    d = Decimal(d)
    re = Decimal(re)

    exp = Decimal(0.1593) * (d**Decimal(-0.105))

    friction = Decimal(0.1034) * d**Decimal(-0.256) * re**Decimal(-exp)

    return friction

  @staticmethod
  def f_factor(n):

    m = HydraulicConstants.exp_loadloss
    n = Decimal(n)

    f = (1/(m+1)) + (1/(2*n)) + ((m-1)**Decimal(0.5)) / (6*(n*n))

    return f