from _decimal import Decimal
from core.domain.entity.actual_irrigation_input import ActualIrrigationBySoilParamsInput
from core.domain.entity.actual_irrigation_input import ActualIrrigationByAtmosphericParamsInput
from core.domain.entity.actual_irrigation_input import IRNmaxInputEntity


class ActualIrrigationNecessaryService:
    @classmethod
    def calculate_max_actual_irrigation(cls, input_entity: IRNmaxInputEntity) -> Decimal:
        theta_fc = input_entity.theta_field_capacity
        theta_wp = input_entity.theta_observed
        z = input_entity.soil_depth
        f_critical = input_entity.f_critical
        return Decimal((theta_fc - theta_wp) * z * f_critical)

    @classmethod
    def calculate_by_atmospheric_params(cls, input_entity: ActualIrrigationByAtmosphericParamsInput) -> Decimal:
        eto = input_entity.actual_evapotranspiration
        kc = input_entity.kc
        pwa = input_entity.percent_wetted_area
        return Decimal(eto * kc * pwa)

    @classmethod
    def calculate_by_soil_params(cls, input_entity: ActualIrrigationBySoilParamsInput) -> Decimal:
        theta_fc = input_entity.theta_field_capacity
        theta_obs = input_entity.theta_observed
        z = input_entity.soil_depth
        return Decimal((theta_fc - theta_obs) * z)
