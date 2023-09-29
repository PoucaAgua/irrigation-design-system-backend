from _decimal import Decimal

from apps.evapotranspiration.reference_evapotranspiration.reference_evapotranspiration_service import (
    ReferenceEvapotranspirationService,
)
from core.domain.entity.evapotranspiration_input import EToHargravesSamaniInput, EToBlanneyCriddleInput, EToPenmanMonteithInput
import pytest
from core.domain.enum.month import MonthEnum
from core.domain.enum.hemisphere import Hemisphere


class TestReferenceEvapotranspirationService:
    error = Decimal("1e-2")

    @pytest.mark.parametrize(
        "temperature_med, temperature_min, temperature_max, latitude, month, expected_result",
        [
            (Decimal("20.0"), Decimal("10.0"), Decimal("30.0"), Decimal("69.0"), MonthEnum.Jan, Decimal("22.165737965964677")),
            # falta adicionar mais :)
        ],
    )
    def test_calculate_by_hargraves_samani(
        self, temperature_med, temperature_min, temperature_max, latitude, month, expected_result
    ):
        # Given
        input_data = EToHargravesSamaniInput(
            temperature_med=temperature_med,
            temperature_min=temperature_min,
            temperature_max=temperature_max,
            latitude=latitude,
            month=month,
        )
        # When
        result = ReferenceEvapotranspirationService.calculate_by_hargraves_samani(input_data)
        # Then
        assert abs(result - expected_result) <= self.error



    @pytest.mark.parametrize(
        "temperature_med, temperature_max, temperature_min, latitude, month, hemisphere, expected_result",
        [
            (Decimal("20.0"),  Decimal("30.0"), Decimal("10.0"),  Decimal("31.0"), MonthEnum.Jan, Hemisphere.NORTE, Decimal("4.11026")),
            # falta adicionar mais :)
        ],
    )
    def test_calculate_by_blaney_criddle(
        self, temperature_med, temperature_max, temperature_min, latitude, month, hemisphere, expected_result
    ):
        # Given
        input_data = EToBlanneyCriddleInput(
            temperature_med=temperature_med,
            temperature_max= temperature_max,
            temperature_min= temperature_min,
            latitude=latitude,
            month=month,
            hemisphere=hemisphere,
            
        )
        # When
        result = ReferenceEvapotranspirationService.calculate_by_blaney_criddle(input_data)
        # Then
        assert abs(result - expected_result) <= self.error



    @pytest.mark.parametrize(
        "temperature_med, temperature_max, temperature_min, days, relative_humidity_air, altitude, wind_speed, ground_heat, daily_radiation, expected_result",
        [
            (20.0, 30.0, 10.0, 30.0, 50.0, 1.0, 20.0, 55.0, 15.0, 20.0, 10.026240268784955 ),
            # falta adicionar mais :)
        ],
    )
    def test_calculate_by_penman_monteith(
        self, temperature_med, temperature_max, temperature_min, relative_humidity_air, altitude, wind_speed, ground_heat, daily_radiation, days, expected_result
    ):
        # Given
        input_data = EToPenmanMonteithInput(
            
            temperature_med=temperature_med,
            temperature_max= temperature_max,
            temperature_min= temperature_min,
            days= days,
            relative_humidity_air=relative_humidity_air,
            altitude=altitude,
            wind_speed=wind_speed,
            ground_heat=ground_heat,
            daily_radiation=daily_radiation
    )
        # When
        result = ReferenceEvapotranspirationService.calculate_by_penman_monteith(input_data)
        # Then
        assert abs(result - expected_result) <= self.error

























































   

    # def test_calculate_hargraves_samani(self):
    #     # Given
    #     test_eto_entity = EToHargravesSamaniInput(
    #         temperature_med=Decimal(20.0),
    #         temperature_min=Decimal(10.0),
    #         temperature_max=Decimal(30.0),
    #         latitude=Decimal(69.0),
    #         month="Jan",
    #     )
    #     expected_result = Decimal(2.83)

    #     # When
    #     result = ReferenceEvapotranspirationService.calculate_by_hargraves_samani(test_eto_entity)

    #     # Then
    #     assert abs(result - expected_result) <= self.error






        

# @staticmethod
#     def calculate_by_penman_monteith(eto_input: EToPenmanMonteithInput) -> Decimal:

#         es = calculate_vapor_saturation_pressure (temperature = eto_input.temperature_med)
#         ea = calculate_vapor_current_pressure(relative_humidity_air = eto_input.relative_humidity_air, vapor_saturation_pressure = es)
#         declivity_curve_pressure_vapor = calculate_declivity_curve_pressure_vapor(temperature = eto_input.temperature_med, vapor_saturation_pressure = es)
#         atmospheric_pressure = calculate_atmospheric_pressure(altitude = eto_input.altitude)
#         psychrometric_constant = calculate_psychrometric_constant(atmospheric_pressure = atmospheric_pressure)
#         u2 = eto_input.wind_speed
#         g = eto_input.ground_heat
#         rn = eto_input.daily_radiation
#         return (0.408 * declivity_curve_pressure_vapor * (rn - g) + (psychrometric_constant * 900 * u2 * (es - ea) / (eto_input.temperature_med + 273))) / (declivity_curve_pressure_vapor + psychrometric_constant * (1 + 0.34 * u2))
