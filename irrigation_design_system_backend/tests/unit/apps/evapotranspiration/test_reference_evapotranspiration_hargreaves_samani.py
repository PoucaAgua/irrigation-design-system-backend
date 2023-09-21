from _decimal import Decimal

import pytest

from apps.evapotranspiration.funcitions_to_reference_evapotranspiration import (
    calculate_radiation_hargreaves_samani,
)
from core.domain.enum.month import MonthEnum_hargraves


class TestReferenceEvapotranspirationHargreavesSamani:
    error = Decimal("1e-2")

    @pytest.mark.parametrize(
        "latitude, month, expected_result",
        [
            (Decimal("69.0"), MonthEnum_hargraves.Jan, Decimal("41.2")),
            (Decimal("69.0"), MonthEnum_hargraves.Fev, Decimal("28.95")),
            (Decimal("69.0"), MonthEnum_hargraves.Mar, Decimal("16.35")),
            (Decimal("69.0"), MonthEnum_hargraves.Abr, Decimal("5.45")),
            (Decimal("69.0"), MonthEnum_hargraves.Maio, Decimal("0.5")),
            (Decimal("69.0"), MonthEnum_hargraves.Jun, Decimal("0")),
            (Decimal("69.0"), MonthEnum_hargraves.Jul, Decimal("0")),
            (Decimal("69.0"), MonthEnum_hargraves.Ago, Decimal("2.7")),
            (Decimal("69.0"), MonthEnum_hargraves.Set, Decimal("11.3")),
            (Decimal("69.0"), MonthEnum_hargraves.Out, Decimal("23.95")),
            (Decimal("69.0"), MonthEnum_hargraves.Nov, Decimal("37.35")),
            (Decimal("69.0"), MonthEnum_hargraves.Dez, Decimal("45")),
            (Decimal("67.0"), MonthEnum_hargraves.Jan, Decimal("41.2")),
            (Decimal("67.0"), MonthEnum_hargraves.Fev, Decimal("28.75")),
            (Decimal("67.0"), MonthEnum_hargraves.Mar, Decimal("16.35")),
            (Decimal("67.0"), MonthEnum_hargraves.Abr, Decimal("5.45")),
            (Decimal("67.0"), MonthEnum_hargraves.Maio, Decimal("0.5")),
            (Decimal("67.0"), MonthEnum_hargraves.Jun, Decimal("0")),
            (Decimal("67.0"), MonthEnum_hargraves.Jul, Decimal("0")),
            (Decimal("67.0"), MonthEnum_hargraves.Ago, Decimal("2.7")),
            (Decimal("67.0"), MonthEnum_hargraves.Set, Decimal("11.3")),
            (Decimal("67.0"), MonthEnum_hargraves.Out, Decimal("23.75")),
            (Decimal("67.0"), MonthEnum_hargraves.Nov, Decimal("37.35")),
            (Decimal("67.0"), MonthEnum_hargraves.Dez, Decimal("45")),
        ],
    )
    def test_calculate_radiation_hargreaves_samani(
        self, latitude: Decimal, month: MonthEnum_hargraves, expected_result: Decimal
    ):
        # When
        result = calculate_radiation_hargreaves_samani(latitude, month)
        print(result)
        # Then
        assert abs(result - expected_result) <= self.error
