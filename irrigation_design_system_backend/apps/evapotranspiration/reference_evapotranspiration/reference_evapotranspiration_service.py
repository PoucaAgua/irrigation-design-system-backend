from _decimal import Decimal

from apps.evapotranspiration.reference_evapotranspiration.percent_daily_solar_hours import (
    calculate_percent_daily_solar_hours,
)
from core.constants.evapotranspiration import ReferenceEvapotranspirationConstants
from core.domain.entity.evapotranspiration.reference.reference_evapotranspiration_input import (
    EToHargravesSamaniInput,
    EToBlanneyCriddleInput,
    EToPenmanMonteithInput,
)
from apps.evapotranspiration.reference_evapotranspiration.solar_radiation import (
    calculate_solar_radiation,
)
from apps.evapotranspiration.reference_evapotranspiration.penman_monteith_method import (
    calculate_vapor_saturation_pressure,
    calculate_vapor_current_pressure,
    calculate_declivity_curve_pressure_vapor,
    calculate_atmospheric_pressure,
    calculate_psychrometric_constant,
)


class ReferenceEvapotranspirationService:
    @staticmethod
    def calculate_by_hargraves_samani(eto_input: EToHargravesSamaniInput) -> Decimal:
        a, b, c, d = ReferenceEvapotranspirationConstants.parameters_hargraves_samani
        radiation = calculate_solar_radiation(latitude=eto_input.latitude, month=eto_input.month)
        temperature_med = eto_input.temperature_med
        temperature_min = eto_input.temperature_min
        temperature_max = eto_input.temperature_max
        return Decimal(
            radiation * a * (b * (temperature_med + c) * (temperature_max - temperature_min)) ** d
        )

    @staticmethod
    def calculate_by_blaney_criddle(eto_input: EToBlanneyCriddleInput) -> Decimal:
        a, b, c = ReferenceEvapotranspirationConstants.parameters_blaney_cridlle
        percent_daily_solar_hours = calculate_percent_daily_solar_hours(
            latitude=eto_input.latitude,
            month=eto_input.month,
            hemisphere=eto_input.hemisphere,
        )
        return Decimal((a * eto_input.temperature_med + b) * percent_daily_solar_hours / c)

    @staticmethod
    def calculate_by_penman_monteith(eto_input: EToPenmanMonteithInput) -> Decimal:
        es = calculate_vapor_saturation_pressure(temperature=eto_input.temperature_med)
        ea = calculate_vapor_current_pressure(
            relative_humidity_air=eto_input.relative_humidity_air,
            vapor_saturation_pressure=es,
        )
        declivity_curve_pressure_vapor = calculate_declivity_curve_pressure_vapor(
            temperature=eto_input.temperature_med, vapor_saturation_pressure=es
        )
        atmospheric_pressure = calculate_atmospheric_pressure(altitude=eto_input.altitude)
        psychrometric_constant = calculate_psychrometric_constant(
            atmospheric_pressure=atmospheric_pressure
        )
        u2 = eto_input.wind_speed
        g = eto_input.ground_heat
        rn = eto_input.daily_radiation
        return (
            0.408 * declivity_curve_pressure_vapor * (rn - g)
            + (psychrometric_constant * 900 * u2 * (es - ea) / (eto_input.temperature_med + 273))
        ) / (declivity_curve_pressure_vapor + psychrometric_constant * (1 + 0.34 * u2))
