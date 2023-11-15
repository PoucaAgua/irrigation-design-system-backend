from _decimal import Decimal
import pytest

from apps.hydraulic_design.special_parts.special_parts_service import SpecialPartsService
from core.domain.entity.special_parts_input import SpecialPartsInput, SpecialPartInput
from core.domain.enum.special_parts_types import SpecialPartsTypes


class TestConsultNominalDiameterTable:
    error = Decimal("1e-2")

    @pytest.mark.parametrize(
        "diameter, types, expected",
        [
            (
                Decimal("1.00"),
                [SpecialPartInput(1, SpecialPartsTypes.Degree_90_Elbow)],
                Decimal("1.5"),
            ),
            (
                Decimal("2.00"),
                [SpecialPartInput(2, SpecialPartsTypes.Open_Gate_Valve)],
                Decimal("1.6"),
            ),
            (
                Decimal("3.00"),
                [SpecialPartInput(10, SpecialPartsTypes.Degree_90_Lateral_Tee)],
                Decimal("80"),
            ),
        ],
    )
    def test_special_parts_load_loss(self, diameter, types, expected):
        special_parts_input = SpecialPartsInput(diameter, types)

        assert (
            Decimal(SpecialPartsService.special_parts_load_loss(special_parts_input))
            - Decimal(expected)
            < self.error
        )
