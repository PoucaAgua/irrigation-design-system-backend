from _decimal import Decimal
from core.constants.evapotranspiration import ReferenceEvapotranspirationConstants
from core.domain.entity.evapotranspiration_entity import (
    EToHargravesSamaniInputyEntity
)
from apps.evapotranspiration.funcitions_to_reference_evapotranspiration import (
    calculate_radiation_hargreaves_samani,
)

parameters_hargraves_samani = ReferenceEvapotranspirationConstants.parameters_hargraves_samani
parameters_blaney_cridlle = ReferenceEvapotranspirationConstants.parameters_blaney_cridlle


class ReferenceEvapotranspirationService:
    @staticmethod
    def calculate_hargraves_samani(eto_entity: EToHargravesSamaniInputyEntity) -> Decimal:
        a, b, c = parameters_hargraves_samani
        Ra = calculate_radiation_hargreaves_samani(
            latitude=eto_entity.latitude, month=eto_entity.month
        )
        Tmed = eto_entity.temperature_med
        Tmin = eto_entity.temperature_min
        Tmax = eto_entity.temperature_max
        return Decimal(Ra * a * (b * (Tmed + c) * (Tmax - Tmin)) ** Decimal(0.5))

    # @staticmethod
    # def calculate_blaney_cridlle(eto_entity: EToBlanneyCriddleInputyEntity)-> Decimal:
    #     a, b, c = parameters_blaney_cridlle
    #     Radiation = calculate_radiation_blaney_criddle(
    #         latitude=eto_entity.latitude,
    #         month=eto_entity.month.value, hemisphere = eto_entity.hemisphere

    #         )
    #     Tmed = calculate_temperature_media(
    #         temperature_media=eto_entity.temperature_med,
    #         temperature_max=eto_entity.temperature_max,
    #         temperature_min=eto_entity.temperature_min,
    #         days=eto_entity.days
    #         )
    #     return Decimal((a * Tmed + b) * Radiation / c)

    # @staticmethod
    # def calculate_penman_monteith(eto_entity: EToPenmanMonteithInputyEntity) -> Decimal:

    #     Tmed = calculate_temperature_media(temperature_max=eto_entity.temperature_max, temperature_min=eto_entity.temperature_min, days=eto_entity.days)
    #     es = calculate_vapor_saturation_pressure (temperature = Tmed)
    #     ea = calculate_vapor_current_pressure(relative_humidity_air = eto_entity.relative_humidity_air, vapor_saturation_pressure = es)
    #     declivity_curve_pressure_vapor = calculate_declivity_curve_pressure_vapor(temperature = Tmed, vapor_saturation_pressure = es)
    #     atmospheric_pressure = calculate_atmospheric_pressure(altitude = eto_entity.altitude)
    #     psychrometric_constant = calculate_psychrometric_constant(atmospheric_pressure = atmospheric_pressure)
    #     u2 = eto_entity.wind_speed
    #     g = eto_entity.ground_heat
    #     rn = eto_entity.daily_radiation
    #     return (0.408 * declivity_curve_pressure_vapor * (rn - g) + (psychrometric_constant * 900 * u2 * (es - ea) / (Tmed + 273))) / (declivity_curve_pressure_vapor + psychrometric_constant * (1 + 0.34 * u2))
