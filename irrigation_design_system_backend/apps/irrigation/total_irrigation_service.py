from _decimal import Decimal

from core.domain.entity.irrigation.total_irrigation_input import (
    TotalIrrigationInput,
)


class TotalIrrigationService:
    @classmethod
    def calculate(cls, total_irrigation_input: TotalIrrigationInput) -> Decimal:
        irn = total_irrigation_input.actual_irrigation
        fl = total_irrigation_input.leaching_fraction
        ea = total_irrigation_input.efficiency
        total_irrigation = irn / ((1 - fl) * ea)
        return Decimal(f"{total_irrigation:.2f}")
