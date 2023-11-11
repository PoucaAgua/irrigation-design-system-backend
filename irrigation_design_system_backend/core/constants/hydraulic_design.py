from _decimal import Decimal


class HydraulicConstants:
    gravity = Decimal(9.81)
    kinematic_viscosity = Decimal(0.000001)
    exp_loadloss = Decimal(1.75)
    flow_exponent = Decimal(0.5)
    coeficient_for_K = Decimal(2.616 * (10) ** (-15))
