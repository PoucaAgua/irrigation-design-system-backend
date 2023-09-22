from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class IRNsoilInputEntity:
    # theta field capacity
    theta_fc: Decimal
    # theta observed
    theta_obs: Decimal
    # soil depth
    z: Decimal


@dataclass
class IRNatmInputEntity:
    eto: Decimal
    kc: Decimal
    # percent wetted area
    pwa: Decimal


@dataclass
class IRNmaxInputEntity:
    theta_fc: Decimal
    theta_wp: Decimal
    z: Decimal
    f_critical: Decimal
