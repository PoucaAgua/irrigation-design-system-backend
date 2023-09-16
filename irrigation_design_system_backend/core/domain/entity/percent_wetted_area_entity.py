from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class IrrigationTreeEntity:
    drippers_number: int
    space_between_lines: Decimal
    space_between_plants: Decimal
    z: Decimal
    q: Decimal
    hydraulic_conductivity_of_saturated_soil: Decimal


@dataclass
class SaturatedWetRadiusX2Entity:
    parameter_model_unsaturated_hydraulic: Decimal
    hydraulic_conductivity_of_saturated_soil: Decimal
    q: Decimal


@dataclass
class ContinuousStripEntity:
    space_between_plants: Decimal
    wetted_zone: Decimal
    row_spacing_plants: Decimal
