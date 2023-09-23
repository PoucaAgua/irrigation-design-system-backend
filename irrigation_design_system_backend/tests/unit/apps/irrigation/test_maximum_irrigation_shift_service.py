from _decimal import Decimal
import pytest

from apps.irrigation.maximum_irrigation_shift_service import MaximumIrrigationShiftService
from apps.irrigation.total_irrigation_service import TotalIrrigationService
from core.domain.entity.irrigation.maximum_irrigation_shift_input import MaximumIrrigationShiftInput
from core.domain.entity.irrigation.total_irrigation_input import TotalIrrigationInput


class TestMaximumIrrigationShiftService:
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                MaximumIrrigationShiftInput(
                    actual_irrigation=10,
                    crop_evapotranspiration=10
                ),
                1,
            ),
            (
                MaximumIrrigationShiftInput(
                    actual_irrigation=20,
                    crop_evapotranspiration=10
                ),
                2,
            ),
        ],
    )
    def test_calculate(self, input_data: MaximumIrrigationShiftInput, expected_output: Decimal):
        result = MaximumIrrigationShiftService.calculate(input_data)
        assert result == expected_output
