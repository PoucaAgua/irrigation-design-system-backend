from _decimal import Decimal
import pytest

from apps.uniformity_and_flow.uniformty_and_flow_service import UniformityAndFlowService
from core.domain.entity.uniformity_and_flow_input import UniformityIrrigationInput


class TestUniformityIrrigation:
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                UniformityIrrigationInput(volume_collected_points=[200, 200, 200, 200]),
                Decimal("100"),
            ),
        ],
    )
    def test_calculate_uniformity(
        self, input_data: UniformityIrrigationInput, expected_output: Decimal
    ):
        result = UniformityAndFlowService.calculate_uniformity(input_data)
        assert result == expected_output
