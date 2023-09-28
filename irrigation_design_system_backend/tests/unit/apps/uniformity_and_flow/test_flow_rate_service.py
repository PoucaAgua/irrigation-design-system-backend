from _decimal import Decimal
import pytest

from apps.uniformity_and_flow.uniformty_and_flow_service import UniformityAndFlowService
from core.domain.entity.uniformity_and_flow_input import FlowRateIrrigationInput


class TestFlowIrrigation:
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                FlowRateIrrigationInput(
                    volume_collected_points=[200] * 16,
                    time=10,
                ),
                Decimal("1.2"),
            ),
        ],
    )
    def test_calculate_flow(self, input_data: FlowRateIrrigationInput, expected_output: Decimal):
        result = UniformityAndFlowService.calculate_flow(input_data)
        assert result == expected_output
