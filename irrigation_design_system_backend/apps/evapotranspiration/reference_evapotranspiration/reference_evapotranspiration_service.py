from _decimal import Decimal

from apps.evapotranspiration.reference_evapotranspiration.blaney_criddle_method import (
    calculate_percent_daily_hours,
)
from apps.evapotranspiration.temperature import calculate_temperature_media
from core.constants.evapotranspiration import ReferenceEvapotranspirationConstants
from core.domain.entity.evapotranspiration_input import (
    EToHargreavesSamaniInput,
    EToBlanneyCriddleInputy,
)
from apps.evapotranspiration.reference_evapotranspiration.hargreaves_samani_method import (
    calculate_radiation_hargreaves_samani,
)

parameters_hargraves_samani = ReferenceEvapotranspirationConstants.parameters_hargraves_samani
parameters_blaney_cridlle = ReferenceEvapotranspirationConstants.parameters_blaney_cridlle


class ReferenceEvapotranspirationService:
    @staticmethod
    def calculate_hargreaves_samani(eto_input: EToHargreavesSamaniInput) -> Decimal:
        a, b, c = parameters_hargraves_samani
        Ra = calculate_radiation_hargreaves_samani(
            latitude=eto_input.latitude, month=eto_input.month
        )
        Tmed = eto_input.temperature_med
        Tmin = eto_input.temperature_min
        Tmax = eto_input.temperature_max
        return Decimal(Ra * a * (b * (Tmed + c) * (Tmax - Tmin)) ** Decimal(0.5))

    @staticmethod
    def calculate_blaney_criddle(eto_input: EToBlanneyCriddleInputy) -> Decimal:
        a, b, c = parameters_blaney_cridlle
        percent_daily_hours = calculate_percent_daily_hours(
            latitude=eto_input.latitude, month=eto_input.month, hemisphere=eto_input.hemisphere
        )
        Tmed = calculate_temperature_media(
            temperature_media=eto_input.temperature_med,
            temperature_max=eto_input.temperature_max,
            temperature_min=eto_input.temperature_min,
            days=eto_input.days,
        )
        return Decimal((a * Tmed + b) * percent_daily_hours / c)

    # @staticmethod
    # def calculate_penman_monteith(eto_input: EToPenmanMonteithInputyEntity) -> Decimal:

    #     Tmed = calculate_temperature_media(temperature_max=eto_input.temperature_max, temperature_min=eto_input.temperature_min, days=eto_input.days)
    #     es = calculate_vapor_saturation_pressure (temperature = Tmed)
    #     ea = calculate_vapor_current_pressure(relative_humidity_air = eto_input.relative_humidity_air, vapor_saturation_pressure = es)
    #     declivity_curve_pressure_vapor = calculate_declivity_curve_pressure_vapor(temperature = Tmed, vapor_saturation_pressure = es)
    #     atmospheric_pressure = calculate_atmospheric_pressure(altitude = eto_input.altitude)
    #     psychrometric_constant = calculate_psychrometric_constant(atmospheric_pressure = atmospheric_pressure)
    #     u2 = eto_input.wind_speed
    #     g = eto_input.ground_heat
    #     rn = eto_input.daily_radiation
    #     return (0.408 * declivity_curve_pressure_vapor * (rn - g) + (psychrometric_constant * 900 * u2 * (es - ea) / (Tmed + 273))) / (declivity_curve_pressure_vapor + psychrometric_constant * (1 + 0.34 * u2))
