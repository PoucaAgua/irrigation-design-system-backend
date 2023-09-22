from _decimal import Decimal

from core.domain.entity.total_irrigation_input import (
    TotalIrrigationByLixiviationFractionInput,
    TotalIrrigationByElectricalConductivityInput,
)


class IrrigationTotalNecessaryService:
    @classmethod
    def __calculate_lixivation_fraction(cls, ce_i: Decimal, ce_e: Decimal) -> Decimal:
        return Decimal(ce_i / (2 * ce_e))

    @classmethod
    def calculate_by_lixiviation_fraction(
        cls, total_irrigation_input: TotalIrrigationByLixiviationFractionInput
    ) -> Decimal:
        irn = total_irrigation_input.actual_irrigation
        ea = total_irrigation_input.ea
        fl = total_irrigation_input.lixiviation_fraction
        return Decimal(irn / ((1 - fl) * ea))

    @classmethod
    def calculate_by_electrical_conductivity(
        cls, total_irrigation_input: TotalIrrigationByElectricalConductivityInput
    ) -> Decimal:
        irn = total_irrigation_input.actual_irrigation
        ce_i = total_irrigation_input.electrical_conductivity_of_irrigation
        ce_e = total_irrigation_input.electrical_conductivity_of_soil_saturation
        ea = total_irrigation_input.efficiency
        return Decimal(irn / ((1 - cls.__calculate_lixivation_fraction(ce_i, ce_e)) * ea))
