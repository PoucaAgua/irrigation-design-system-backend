import pytest
from _decimal import Decimal
from core.domain.entity.evapotranspiration.crop_evapotranspiration_input import (
    CropEvapotranspirationInput,
)
from apps.evapotranspiration.crop_evapotranspiration.crop_evapotranspiration_service import (
    CropEvapotranspirationService,
)


class TestCropEvapotranspirationService:
    error = Decimal("0.01")

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                CropEvapotranspirationInput(
                    Eto=Decimal("10.0"),
                    Kc=Decimal("12.0"),
                    Kl=Decimal("3.0"),
                    P=Decimal("5.0"),
                ),
                Decimal("528"),
            ),
        ],
    )
    def test_calculate_by_keller(self, input_data: CropEvapotranspirationInput, expected_output):
        result = CropEvapotranspirationService.etc_by_keller(input_data)
        assert round(result, 6) == round(expected_output, 6)

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                CropEvapotranspirationInput(
                    Eto=Decimal("10.0"),
                    Kc=Decimal("12.0"),
                    Kl=Decimal("3.0"),
                    P=Decimal("5.0"),
                ),
                Decimal("6"),
            ),
        ],
    )
    def test_calculate_by_bernardo(self, input_data: CropEvapotranspirationInput, expected_output):
        result = CropEvapotranspirationService.etc_by_bernardo(input_data)
        assert round(result, 6) == round(expected_output, 6)

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                CropEvapotranspirationInput(
                    Eto=Decimal("10.0"),
                    Kc=Decimal("12.0"),
                    Kl=Decimal("3.0"),
                    P=Decimal("5.0"),
                ),
                Decimal("6"),
            ),
        ],
    )
    def test_calculate_by_fereres(self, input_data: CropEvapotranspirationInput, expected_output):
        result = CropEvapotranspirationService.etc_by_fereres(input_data)
        assert round(result, 6) == round(expected_output, 6)

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                CropEvapotranspirationInput(
                    Eto=Decimal("10.0"),
                    Kc=Decimal("12.0"),
                    Kl=Decimal("3.0"),
                    P=Decimal("5.0"),
                ),
                Decimal("26.832815729997478"),
            ),
        ],
    )
    def test_calculate_by_keller_and_bliesner(
        self, input_data: CropEvapotranspirationInput, expected_output
    ):
        result = CropEvapotranspirationService.etc_by_keller_and_bliesner(input_data)
        assert round(result, 6) == round(expected_output, 6)
