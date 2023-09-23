from _decimal import Decimal
from core.domain.entity.actual_irrigation_input import ActualIrrigationBySoilParamsInput
from core.domain.entity.actual_irrigation_input import ActualIrrigationByAtmosphericParamsInput
from core.domain.entity.actual_irrigation_input import MaxActualIrrigationInput


class ActualIrrigationService:
    @classmethod
    def calculate_max_actual_irrigation(
        cls, max_actual_irrigation_input: MaxActualIrrigationInput
    ) -> Decimal:
        fraction_of_total_wetted_area = max_actual_irrigation_input.fraction_of_total_wetted_area

        max_actual_irrigation = cls.calculate_by_soil_params(
            ActualIrrigationBySoilParamsInput(**max_actual_irrigation_input.dict())
        )
        return max_actual_irrigation * fraction_of_total_wetted_area

    @classmethod
    def calculate_by_atmospheric_params(
        cls, input_entity: ActualIrrigationByAtmosphericParamsInput
    ) -> Decimal:
        eto = input_entity.actual_evapotranspiration
        kc = input_entity.kc
        pwa = input_entity.percent_wetted_area
        return Decimal(eto * kc * pwa)

    @classmethod
    def calculate_by_soil_params(
        cls, actual_irrigation_input: ActualIrrigationBySoilParamsInput
    ) -> Decimal:
        theta_fc = actual_irrigation_input.soil_moisture_field_capacity
        theta_pwp = actual_irrigation_input.soil_moisture_at_permanent_wilting_point
        z = 10 * actual_irrigation_input.soil_depth
        f = actual_irrigation_input.depletion_factor
        effective_precipitation = actual_irrigation_input.effective_precipitation or 0
        return max(Decimal((theta_fc - theta_pwp) * z * f) - effective_precipitation, 0)
