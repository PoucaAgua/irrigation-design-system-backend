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
            (20.0, 2.338281270927446),
            (25.0, 3.1677777175068473),
            (15.0, 1.7053462321157722),
            (10.0, 1.2279626193393784),
            (35.0,  5.622681238496122),
            (40.0, 7.375613593062048),
            (5.0, 0.8723109603497123),
            (12.5, 1.4494811248284514),
            (22.5, 2.725587606605459),
            (17.5, 1.9999869748999506),
            (32.0,  4.754775396261813),
            (28.0, 3.779930363995263),
            (37.5, 6.447730885163706),
            (18.0, 2.063989202660485),
            (8.0, 1.0727688258811263),
        ],
    )
    def test_calculate_vapor_saturation_pressure(self, temperature, expected_result):
        result = calculate_vapor_saturation_pressure(temperature)
        assert math.isclose(result, expected_result, rel_tol=self.error)


    @pytest.mark.parametrize(
        "relative_humidity_air, temperature, expected_result",
        [
            (44, 20, 1.0288437592080764),
            (44, 30, 1.8669486258539658),
            (40, 10, 0.4911850477357514),
            (45, 15, 0.7674058044520975),
            (50, 20, 1.169140635463723),
            (55, 25, 1.7422777446287663),
            (65, 35.1, 3.6749912860891976),
            (42.7, 12.8, 0.6312290294788812),
            (47.4, 17.3,  0.936091630785933),
            (52.9, 22.6, 1.450613510554012),
            (57.6, 27.4, 2.1023237721503225),
            (62.3, 32.0, 2.9622250718711096),
            (44.8, 18.7,  0.9661576870738966),
            (49.5, 23.3, 1.416106459195399),
            (40.5, 10.5, 0.5142353409741444),
        ],
    )
    def test_calculate_vapor_current_pressure(
        self, relative_humidity_air, temperature, expected_result
    ):
        vapor_saturation_pressure = calculate_vapor_saturation_pressure(temperature)
        result = calculate_vapor_current_pressure(relative_humidity_air, vapor_saturation_pressure)
        assert math.isclose(result, expected_result, rel_tol=self.error)

    @pytest.mark.parametrize(
        "temperature, expected_result",
        [
            (20.0,  0.14474018811241365),
            (25.0,  0.18868182684282603),
            (24.3,  0.1819258849472823),
            (33.0,  0.2821373665384726),
            (34.0,  0.29615809125881837),
            (33.4,  0.28767750418502946),
            (37.1,  0.3433754998926738),
            (25.82,  0.19686355139434455),
            (40.2,  0.3967071106994992),
            (45.3,  0.49934253092170255),
            (46.1,   0.5172750948020735),
            (24.87,  0.1874114160718771),
            (29.65,   0.23914527717516107),
            (45.80,  0.5104890154668869),
            (21.32,  0.15539975161896216),

        ],
    )
    def test_calculate_declivity_curve_pressure_vapor(
        self, temperature, expected_result
    ):
        vapor_saturation_pressure = calculate_vapor_saturation_pressure(temperature)
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

