from _decimal import Decimal

from apps.hydraulic_design.derivationline.derivationline_calculate_service import (
    DerivationLineService,
)
from core.domain.entity.derivation_line_input import (
    DerivationLineDiameterInput,
    DerivationLineLoadLossInput,
)


class TestDerivationLineService:
    error = Decimal("1e-3")

    def test_calculate_diameter(self):
        test_derivation_line_entity = DerivationLineDiameterInput(
            demand_flow=Decimal(0.008481),
            speed_max=Decimal(1.5),
        )
        expected = float(100)

        result = DerivationLineService.calculate_diameter(test_derivation_line_entity)

        assert expected == result

    def calculate_load_loss_derivation_line(self):
        test_load_loss_entity = DerivationLineLoadLossInput(
            length_derivation_line=Decimal(50.0),
            diameter_derivation_line=Decimal(0.1),
            flow=Decimal(1.079834458),
            n_outputs=Decimal(62.5),
        )
        expected = Decimal(0.19613492804)
        result = DerivationLineService.calculate_load_loss(test_load_loss_entity)

        assert abs(expected - result) <= self.error
