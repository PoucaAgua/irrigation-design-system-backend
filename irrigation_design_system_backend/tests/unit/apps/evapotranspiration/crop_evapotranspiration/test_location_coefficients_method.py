import pytest
from decimal import Decimal
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
                Decimal("2.0"),
                Decimal("1.85"),
            ),
            (
                Decimal("5.0"),
                Decimal("4.4"),
            ),
            (
                Decimal("8.0"),
                Decimal("6.95"),
            ),
            (
                Decimal("20.0"),
                Decimal("17.15"),
            ),
            (
                Decimal("15.0"),
                Decimal("12.9"),
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
                Decimal("2.0"),
                Decimal("0.02"),
            ),
            (
                Decimal("5.0"),
                Decimal("0.05"),
            ),
            (
                Decimal("8.0"),
                Decimal("0.08"),
            ),
            (
                Decimal("20.0"),
                Decimal("0.2"),
            ),
            (
                Decimal("15.0"),
                Decimal("0.15"),
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
                Decimal("2.0"),
                Decimal("0.02"),
            ),
            (
                Decimal("5.0"),
                Decimal("0.05"),
            ),
            (
                Decimal("8.0"),
                Decimal("0.08"),
            ),
            (
                Decimal("20.0"),
                Decimal("0.2"),
            ),
            (
                Decimal("15.0"),
                Decimal("0.15"),
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
                Decimal("2.0"),
                Decimal("0.14142135623730953"),
            ),
            (
                Decimal("5.0"),
                Decimal("0.223606797749979"),
            ),
            (
                Decimal("8.0"),
                Decimal("0.28284271247461906"),
            ),
            (
                Decimal("20.0"),
                Decimal("0.447213595499958"),
            ),
            (
                Decimal("15.0"),
                Decimal("0.3872983346207417"),
            ),
        ],
    )
    def test_calculate_by_keller_and_bliesner(self, P, expected_result):
        result = calculate_by_keller_and_bliesner(P)
        assert math.isclose(result, expected_result, rel_tol=self.error)
