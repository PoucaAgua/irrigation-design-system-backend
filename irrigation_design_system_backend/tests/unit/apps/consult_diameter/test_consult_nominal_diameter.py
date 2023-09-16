from _decimal import Decimal
import pytest

from apps.hydraulic_design.consult_diameter.consult_nominal_diameter import ConsultNominalDiameterTable

class TestConsultNominalDiameterTable:
    @pytest.mark.parametrize("test, expected", [
        (101.0, 125.0),
        (100.0, 100.0),
        (20.0, 35.0)
    ])
    def test_nominal_diameter(self, test, expected):
        assert (
            Decimal(ConsultNominalDiameterTable.nominal_diameter(test))
            == Decimal(expected)
        )
