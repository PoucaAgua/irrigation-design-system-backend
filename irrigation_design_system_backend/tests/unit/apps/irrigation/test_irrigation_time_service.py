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
                    itn=5,
                    sp=2,
                    sl=3,
                    Ne=1,
                    q=18,
                ),
                Decimal("1.666666666666666666666666667"),
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
                    itn=5,
                    se=0.2,
                    sl=1,
                    q=1.24,
                ),
                Decimal("0.8064516129032258064516129032"),
            ),
        ],
    )
    def test_calculate_by_line(
        self, input_data: IrrigationTimeByLineInput, expected_output: Decimal
    ):
        result = IrrigationTimeService.calculate_by_line_params(input_data)
        assert result == expected_output
