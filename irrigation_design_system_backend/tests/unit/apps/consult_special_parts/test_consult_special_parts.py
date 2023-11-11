import pytest
from apps.hydraulic_design.consult_special_parts.consult_loadloss_specialparts import (
    ConsultLoadLossSpecialPartsTable,
)


class TestConsultNominalDiameterTable:
    @pytest.mark.parametrize(
        "diameter, types, expected",
        [
            (0.50, "Degree_90_Elbow", 1.1),
            (0.75, "Degree_45_Bend", 0.3),
            (1.00, "Degree_90_Double_Branch_Tee", 3.1),
            (1.25, "Lightweight_Check_Valv", "error"),
            (0.330, "Open_Angle_Valve", "error"),
            (5.223, "Degree_90_Elbow", "error"),
        ],
    )
    def test_loadloss_special_parts(self, diameter, types, expected):
        if expected == "error":
            with pytest.raises(ValueError):
                ConsultLoadLossSpecialPartsTable.loadloss_special_parts(types, diameter)

        else:
            assert (
                ConsultLoadLossSpecialPartsTable.loadloss_special_parts(types, diameter) == expected
            )
