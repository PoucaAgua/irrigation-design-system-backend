from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class ActualIrrigationBySoilParamsInput:
    theta_field_capacity: Decimal
    theta_observed: Decimal
    soil_depth: Decimal


@dataclass
class ActualIrrigationByAtmosphericParamsInput:
    actual_evapotranspiration: Decimal
    kc: Decimal
    percent_wetted_area: Decimal


@dataclass
class IRNmaxInputEntity(ActualIrrigationBySoilParamsInput):
    f_critical: Decimal
