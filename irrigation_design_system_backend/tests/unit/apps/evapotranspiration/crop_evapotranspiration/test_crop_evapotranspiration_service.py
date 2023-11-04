import pytest
from _decimal import Decimal
from core.domain.entity.crop_evapotranspiration_input import ETcInput
from apps.evapotranspiration.crop_evapotranspiration.crop_evapotranspiration_service import (
    CropEvapotranspirationService,
)


class TestCropEvapotranspirationService:
    error = Decimal("0.01")

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                ETcInput(P=Decimal("2.0")),
                Decimal("1.85"),
            ),
            (
                ETcInput(P=Decimal("5.0")),
                Decimal("4.4"),
            ),
            (
                ETcInput(P=Decimal("8.0")),
                Decimal("6.95"),
            ),
            (
                ETcInput(P=Decimal("20.0")),
                Decimal("17.15"),
            ),
            (
                ETcInput(P=Decimal("15.0")),
                Decimal("12.9"),
            ),
        ],
    )
    def test_calculate_by_keller(self, input_data, expected_output):
        result = CropEvapotranspirationService.calculate_by_keller(input_data)
        assert abs(result - expected_output) <= self.error

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                ETcInput(P=Decimal("2.0")),
                Decimal("0.02"),
            ),
            (
                ETcInput(P=Decimal("5.0")),
                Decimal("0.05"),
            ),
            (
                ETcInput(P=Decimal("8.0")),
                Decimal("0.08"),
            ),
            (
                ETcInput(P=Decimal("20.0")),
                Decimal("0.2"),
            ),
            (
                ETcInput(P=Decimal("15.0")),
                Decimal("0.15"),
            ),
        ],
    )
    def test_calculate_by_bernardo(self, input_data, expected_output):
        result = CropEvapotranspirationService.calculate_by_bernardo(input_data)
        assert abs(result - expected_output) <= self.error

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                ETcInput(P=Decimal("2.0")),
                Decimal("0.02"),
            ),
            (
                ETcInput(P=Decimal("5.0")),
                Decimal("0.05"),
            ),
            (
                ETcInput(P=Decimal("8.0")),
                Decimal("0.08"),
            ),
            (
                ETcInput(P=Decimal("20.0")),
                Decimal("0.2"),
            ),
            (
                ETcInput(P=Decimal("15.0")),
                Decimal("0.15"),
            ),
        ],
    )
    def test_calculate_by_fereres(self, input_data, expected_output):
        result = CropEvapotranspirationService.calculate_by_fereres(input_data)
        assert abs(result - expected_output) <= self.error

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                ETcInput(P=Decimal("2.0")),
                Decimal("0.14142135623730953"),
            ),
            (
                ETcInput(P=Decimal("5.0")),
                Decimal("0.223606797749979"),
            ),
            (
                ETcInput(P=Decimal("8.0")),
                Decimal("0.28284271247461906"),
            ),
            (
                ETcInput(P=Decimal("20.0")),
                Decimal("0.447213595499958"),
            ),
            (
                ETcInput(P=Decimal("15.0")),
                Decimal("0.3872983346207417"),
            ),
        ],
    )
    def test_calculate_by_keller_and_bliesner(self, input_data, expected_output):
        result = CropEvapotranspirationService.calculate_by_keller_and_bliesner(input_data)
        assert abs(result - expected_output) <= self.error
