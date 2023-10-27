import math
import pytest
from apps.evapotranspiration.reference_evapotranspiration.penman_monteith_method import (
    calculate_vapor_saturation_pressure,
    calculate_vapor_current_pressure,
    calculate_declivity_curve_pressure_vapor,
    calculate_atmospheric_pressure,
    calculate_psychrometric_constant,
)


class TestEvapotranspirationFunctions:
    error = 1e-5

    @pytest.mark.parametrize(
        "temperature, expected_result",
        [
            (20.0, 2.339),
            (25.0, 3.167),
            (15.0, 1.705),
            (10.0, 1.227),
            (0.0, 0.610),
            (35.0, 5.662),
            (40.0, 7.375),
            (5.0, 0.872),
            (12.5, 1.449),
            (22.5, 2.725),
            (17.5, 1.999),
            (32.0, 4.754),
            (28.0, 3.779),
            (37.5, 6.274),
            (18.0, 2.063),
            (8.0, 1.072),
            (27.5, 3.671),
            (21.5, 2.564),
            (33.5, 5.172),
        ],
    )
    def test_calculate_vapor_saturation_pressure(self, temperature, expected_result):
        result = calculate_vapor_saturation_pressure(temperature)
        assert math.isclose(result, expected_result, rel_tol=self.error)

    @pytest.mark.parametrize(
        "relative_humidity_air, vapor_saturation_pressure, expected_result",
        [
            (44.8, 2.339, 1.047)(31.6, 3.167, 1.002)(30.0, 1.705, 0.512)(59.1, 1.227, 0.725)(
                77.2, 0.610, 0.471
            )(56.3, 5.662, 3.190)(34.9, 7.375, 2.575)(42.8, 0.872, 0.373)(78.2, 1.449, 1.134)(
                49.9, 2.725, 1.360
            )(
                53.1, 1.999, 1.061
            )(
                39.9, 4.754, 1.896
            )(
                67.3, 3.779, 2.542
            )(
                46.5, 6.274, 2.916
            )(
                63.9, 2.063, 1.319
            )(
                67.6, 1.072, 0.725
            )(
                35.0, 3.671, 1.286
            )(
                73.9, 2.564, 1.896
            )(
                48.2, 5.172, 2.495
            )
        ],
    )
    def test_calculate_vapor_current_pressure(
        self, relative_humidity_air, vapor_saturation_pressure, expected_result
    ):
        result = calculate_vapor_current_pressure(relative_humidity_air, vapor_saturation_pressure)
        assert math.isclose(result, expected_result, rel_tol=self.error)

    @pytest.mark.parametrize(
        "temperature, vapor_saturation_pressure, expected_result",
        [
            (23.46, 2.339, 0.1410)(20.40, 3.167, 0.1954)(30.40, 1.705, 0.0975)(
                39.38, 1.227, 0.0657
            )(25.10, 0.610, 0.0363)(41.72, 5.662, 0.2980)(41.09, 7.375, 0.3900)(
                37.35, 0.872, 0.0474
            )(
                21.16, 1.449, 0.0889
            )(
                29.31, 2.725, 0.1571
            )(
                33.34, 1.999, 0.1118
            )(
                28.68, 4.754, 0.2754
            )(
                39.12, 3.779, 0.2027
            )(
                27.27, 6.274, 0.3673
            )(
                33.36, 2.063, 0.1154
            )(
                23.88, 1.072, 0.0644
            )(
                24.46, 3.671, 0.2196
            )(
                39.06, 2.564, 0.1376
            )(
                20.52, 5.172, 0.3188
            )
        ],
    )
    def test_calculate_declivity_curve_pressure_vapor(
        self, temperature, vapor_saturation_pressure, expected_result
    ):
        result = calculate_declivity_curve_pressure_vapor(temperature, vapor_saturation_pressure)
        assert math.isclose(result, expected_result, rel_tol=self.error)

    @pytest.mark.parametrize(
        "altitude, expected_result",
        [
            (0.73, 807843015984735.25),
            (123.43, 807803763700173.50),
            (37.17, 807831357067597.88),
            (85.13, 807816017521964.75),
            (75.22, 807819185358763.12),
            (59.38, 807824254220477.25),
            (179.53, 807785818577381.25),
            (37.68, 807831196423074.38),
            (45.42, 807828718262667.38),
            (149.67, 807795372186906.75),
            (153.43, 807794168569185.25),
            (181.43, 807785212464642.12),
            (86.77, 807815490455727.25),
            (198.55, 807779734747765.50),
            (42.68, 807829594565021.50),
        ],
    )
    def test_calculate_atmospheric_pressure(self, altitude, expected_result):
        result = calculate_atmospheric_pressure(altitude)
        assert math.isclose(result, expected_result, rel_tol=self.error)

    @pytest.mark.parametrize(
        "atmospheric_pressure, expected_result",
        [
            (807843015984735.2, 537215605629.84894),
            (807803763700173.5, 537189502860.61536),
            (807831357067597.9, 537207852449.9526),
            (807816017521964.8, 537197651652.10657),
            (807819185358763.1, 537199758263.5775),
            (807824254220477.2, 537203129056.6174),
            (807785818577381.2, 537177569353.95856),
            (807831196423074.4, 537207745621.3445),
            (807828718262667.4, 537206097644.6738),
            (807795372186906.8, 537183922504.29297),
            (807794168569185.2, 537183122098.5082),
            (807785212464642.1, 537177166288.987),
            (807815490455727.2, 537197301153.05865),
            (807779734747765.5, 537173523607.26404),
            (807829594565021.5, 537206680385.7393),
        ],
    )
    def test_calculate_psychrometric_constant(self, atmospheric_pressure, expected_result):
        result = calculate_psychrometric_constant(atmospheric_pressure)
        assert math.isclose(result, expected_result, rel_tol=self.error)
