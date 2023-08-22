from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class IRNsoloProjectionInputEntity:
    umidade_cc: Decimal
    umidade_atual: Decimal
    profudidade: Decimal


@dataclass
class IRNatmProjectionInputEntity:
    evapo_eto: Decimal
    coef_cultura: Decimal
    area_molhada: Decimal

@dataclass
class IRNmaxProjectionInputEntity:
    theta_cc: Decimal
    theta_pm: Decimal
    profunidade: Decimal
    f_critico: Decimal

