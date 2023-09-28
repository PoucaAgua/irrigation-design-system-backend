from _decimal import Decimal
import pytest

from apps.irrigation.irrigation_time_service import IrrigationTimeService
from core.domain.entity.irrigation.irrigation_time_input import (
    IrrigationTimeByLineInput,
    IrrigationTimeByPlantInput,
)


class TestIrrigationTime:
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                IrrigationTimeByPlantInput(
                    total_irrigation=5,
                    spacing_between_plants=2,
                    spacing_between_side_lines=3,
                    number_of_emitters_per_plant=1,
                    emitter_flow=18,
                ),
                Decimal("1.67"),
            ),
        ],
    )
    def test_calculate_by_plant(
        self, input_data: IrrigationTimeByPlantInput, expected_output: Decimal
    ):
        result = IrrigationTimeService.calculate_by_plant_params(input_data)
        assert result == expected_output

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                IrrigationTimeByLineInput(
                    total_irrigation=5,
                    spacing_between_emitters=0.2,
                    spacing_between_side_lines=1,
                    emitter_flow=1.24,
                ),
                Decimal("0.81"),
            ),
        ],
    )
    def test_calculate_by_line(
        self, input_data: IrrigationTimeByLineInput, expected_output: Decimal
    ):
        result = IrrigationTimeService.calculate_by_line_params(input_data)
        assert result == expected_output
