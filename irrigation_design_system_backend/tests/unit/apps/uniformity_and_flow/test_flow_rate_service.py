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
                    v1=200,
                    v2=200,
                    v3=200,
                    v4=200,
                    v5=200,
                    v6=200,
                    v7=200,
                    v8=200,
                    v9=200,
                    v10=200,
                    v11=200,
                    v12=200,
                    v13=200,
                    v14=200,
                    v15=200,
                    v16=200,
                    time_c=10,
            ),
                Decimal("1.2"),
            ),
        ],
    )
    def test_calculate_flow(self, input_data: FlowRateIrrigationInput, expected_output: Decimal):
        result = UniformityAndFlowService.calculate_flow(input_data)
        assert result == expected_output