from _decimal import Decimal

from apps.hydraulic_design.calculate_lateral_line.calculate_lateral_line import (
    LateralLineService
)
from core.domain.entity.lateral_line_entity import (
    LateralLineInput,
)


class TestLateralLineService:

    def test_calculate_diameter(self):
        error = Decimal("1e-3")

        test_lateral_line_entity = LateralLineInput(
            internal_diameter=Decimal(0.016),
            service_pressure=Decimal(10),
            nominal_flow_rate=Decimal(1.6),
            max_flow_rate_variation=Decimal(0.05),
            emitter_spacing=Decimal(0.2),
            flow_exponent=Decimal(0.5),
            exponent_pressure_loss_equation=Decimal(1.75),
            coefficient=Decimal(8.87295e-7),
        )

        expected = Decimal(61.06133924)

        result = LateralLineService.calculate_length_lateral_line(test_lateral_line_entity)

        assert abs(expected - result) < error
