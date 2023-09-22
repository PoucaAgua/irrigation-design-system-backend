from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class TotalIrrigationByLixiviationFractionInput:
    actual_irrigation: Decimal
    lixiviation_fraction: Decimal
    ea: Decimal


@dataclass
class TotalIrrigationByElectricalConductivityInput:
    actual_irrigation: Decimal
    electrical_conductivity_of_irrigation: Decimal
    electrical_conductivity_of_soil_saturation: Decimal
    efficiency: Decimal
