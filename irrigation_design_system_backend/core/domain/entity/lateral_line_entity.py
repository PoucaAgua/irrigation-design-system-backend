from decimal import Decimal
from dataclasses import dataclass


@dataclass
class LateralLineInput:
    service_pressure: Decimal
    nominal_flow_rate: Decimal
    max_flow_rate_variation: Decimal
    internal_diameter: Decimal
    emitter_spacing: Decimal
    flow_exponent: Decimal
    exponent_pressure_loss_equation: Decimal

@dataclass
class LateralLineHeadLossInput:
    length_lateral_line: Decimal
    internal_diameter: Decimal
    nominal_flow_rate: Decimal
    exponent_pressure_loss_equation: Decimal
    emitter_spacing: Decimal
