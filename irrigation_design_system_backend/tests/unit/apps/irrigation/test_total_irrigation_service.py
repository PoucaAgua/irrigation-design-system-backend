from _decimal import Decimal
import pytest

from apps.irrigation.total_irrigation_service import TotalIrrigationService
from core.domain.entity.irrigation.total_irrigation_input import TotalIrrigationInput


class TestTotalIrrigationService:
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                TotalIrrigationInput(
                    actual_irrigation=20,
                    electrical_conductivity_of_irrigation=11,
                    electrical_conductivity_of_soil_saturation=12,
                    efficiency=0.8,
                ),
                Decimal("46.15"),
            ),
            (
                TotalIrrigationInput(
                    actual_irrigation=20,
                    leaching_fraction=0.2,
                    efficiency=0.8,
                ),
                Decimal("31.25"),
            ),
        ],
    )
    def test_calculate(self, input_data: TotalIrrigationInput, expected_output: Decimal):
        result = TotalIrrigationService.calculate(input_data)
        assert result == expected_output
