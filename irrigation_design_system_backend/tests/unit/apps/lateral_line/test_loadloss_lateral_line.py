from _decimal import Decimal
from apps.hydraulic_design.calculate_lateral_line.calculate_lateral_line import LateralLineService
from core.domain.entity.lateral_line_entity import LateralLineHeadLossInput


class TestLateralLineService:
    def test_calculate_head_loss(self):
        error = Decimal("1e-3")
        test_lateral_line_entity = LateralLineHeadLossInput(
            length_lateral_line=Decimal(61.0613),
            internal_diameter=Decimal(0.016),
            emitter_spacing=Decimal(0.2),
            nominal_flow_rate=Decimal(1.6),
        )
        expected = Decimal(0.982720192)
        result = LateralLineService.calculate_head_loss(test_lateral_line_entity)
        assert abs(expected - result) <= error
