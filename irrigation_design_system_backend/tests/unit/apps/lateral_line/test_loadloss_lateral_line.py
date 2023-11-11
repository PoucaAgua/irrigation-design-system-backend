from _decimal import Decimal

from apps.hydraulic_design.calculate_lateral_line.calculate_lateral_line import LateralLineService
from core.domain.entity.lateral_line_entity import LateralLineInput


class TestLateralLineService:
    def test_calculate_head_loss(self):
        error = Decimal("1e-3")

        test_lateral_line_entity = LateralLineInput(
            friction_factor=Decimal(0.030),
            water_velocity_lateral_line=Decimal(0.6748),
            factor_f=Decimal(0.36),
            gravity_acceleration=Decimal(9.81),
        )

        expected = Decimal(2.260)

        result = LateralLineService.calculate_head_loss(test_lateral_line_entity)

        assert abs(expected - result) <= error
