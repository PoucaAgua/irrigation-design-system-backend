import pytest
from _decimal import Decimal
import math
from apps.evapotranspiration.crop_evapotranspiration.location_coefficients_method import (
    calculate_by_keller,
    calculate_by_bernardo,
    calculate_by_fereres,
    calculate_by_keller_and_bliesner,
)


class TestLocationCoefficients:
    error = Decimal("0.01")

    @pytest.mark.parametrize(
        "P, expected_result",
        [
            (
                2.0,
                1.85,
            ),
            (
                5.0,
                4.4,
            ),
            (
                8.0,
                6.95,
            ),
            (
                20.0,
                17.15,
            ),
            (
                15.0,
                12.9,
            ),
        ],
    )
    def test_calculate_by_keller(self, P, expected_result):
        result = calculate_by_keller(P)
        assert math.isclose(result, expected_result, rel_tol=self.error)

    @pytest.mark.parametrize(
        "P, expected_result",
        [
            (
                2.0,
                0.02,
            ),
            (
                5.0,
                0.05,
            ),
            (
                8.0,
                0.08,
            ),
            (
                20.0,
                0.2,
            ),
            (
                15.0,
                0.15,
            ),
        ],
    )
    def test_calculate_by_bernardo(self, P, expected_result):
        result = calculate_by_bernardo(P)
        assert math.isclose(result, expected_result, rel_tol=self.error)

    @pytest.mark.parametrize(
        "P, expected_result",
        [
            (
                2.0,
                0.02,
            ),
            (
                5.0,
                0.05,
            ),
            (
                8.0,
                0.08,
            ),
            (
                20.0,
                0.2,
            ),
            (
                15.0,
                0.15,
            ),
        ],
    )
    def test_calculate_by_fereres(self, P, expected_result):
        result = calculate_by_fereres(P)
        assert math.isclose(result, expected_result, rel_tol=self.error)

    @pytest.mark.parametrize(
        "P, expected_result",
        [
            (
                2.0,
                0.14142135623730953,
            ),
            (
                5.0,
                0.223606797749979,
            ),
            (
                8.0,
                0.28284271247461906,
            ),
            (
                20.0,
                0.447213595499958,
            ),
            (
                15.0,
                0.3872983346207417,
            ),
        ],
    )
    def test_calculate_by_keller_and_bliesner(self, P, expected_result):
        result = calculate_by_keller_and_bliesner(P)
        assert math.isclose(result, expected_result, rel_tol=self.error)
