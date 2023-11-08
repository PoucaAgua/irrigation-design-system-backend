from _decimal import Decimal
import pytest

from apps.hydraulic_design.consult_special_parts.consult_loadloss_specialparts import ConsultLoadLossSpecialPartsTable

class TestConsultNominalDiameterTable:
    @pytest.mark.parametrize("diameter, types, expected", [
        (0.50, 'joelho_90', 1.1),
        (0.75, 'curva_45', 0.3),
        (1.00, 'tê_90_saida_bilateral', 3.1),
        (1.25, 'valvula_retenção_tipo_leve', 4.9),
        (1.50, 'registro_angulo_aberto', 17)

    ])
    def test_loadloss_special_parts(self, diameter, types,expected):
        assert (
            Decimal(ConsultLoadLossSpecialPartsTable.loadloss_special_parts(types, diameter))
            == Decimal(expected)
        )
