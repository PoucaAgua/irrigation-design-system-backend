from _decimal import Decimal
import pytest

from apps.uniformity_and_flow.uniformty_and_flow_service import UniformityAndFlowService
from core.domain.entity.uniformity_and_flow_input import UniformityIrrigationInput

class TestUniformityIrrigation:
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                UniformityIrrigationInput(
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
                ),
                Decimal("100"),
            ),
        ],
    )
    def test_calculate_uniformity(self, input_data: UniformityIrrigationInput, expected_output: Decimal):
        result = UniformityAndFlowService.calculate_uniformity(input_data)
        assert result == expected_output