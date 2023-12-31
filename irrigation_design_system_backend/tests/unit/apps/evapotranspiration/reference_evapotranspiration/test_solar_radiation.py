from _decimal import Decimal
import pytest

from apps.evapotranspiration.reference_evapotranspiration.solar_radiation import (
    calculate_solar_radiation,
)
from core.domain.enum.month import MonthEnum


class TestSolarRadiation:
    error = Decimal("1e-2")

    @pytest.mark.parametrize(
        "latitude, month, expected_result",
        [
            (Decimal("69.0"), MonthEnum.Jan, Decimal("41.2")),
            (Decimal("69.0"), MonthEnum.Fev, Decimal("28.95")),
            (Decimal("69.0"), MonthEnum.Mar, Decimal("16.35")),
            (Decimal("69.0"), MonthEnum.Abr, Decimal("5.45")),
            (Decimal("69.0"), MonthEnum.Mai, Decimal("0.5")),
            (Decimal("69.0"), MonthEnum.Jun, Decimal("0")),
            (Decimal("69.0"), MonthEnum.Jul, Decimal("0")),
            (Decimal("69.0"), MonthEnum.Ago, Decimal("2.7")),
            (Decimal("69.0"), MonthEnum.Set, Decimal("11.3")),
            (Decimal("69.0"), MonthEnum.Out, Decimal("23.95")),
            (Decimal("69.0"), MonthEnum.Nov, Decimal("37.35")),
            (Decimal("69.0"), MonthEnum.Dez, Decimal("45")),
            (Decimal("67.0"), MonthEnum.Jan, Decimal("40.95")),
            (Decimal("67.0"), MonthEnum.Fev, Decimal("29.65")),
            (Decimal("67.0"), MonthEnum.Mar, Decimal("17.5")),
            (Decimal("67.0"), MonthEnum.Abr, Decimal("6.6")),
            (Decimal("67.0"), MonthEnum.Mai, Decimal("1.15")),
            (Decimal("67.0"), MonthEnum.Jun, Decimal("0.05")),
            (Decimal("67.0"), MonthEnum.Jul, Decimal("0.25")),
            (Decimal("67.0"), MonthEnum.Ago, Decimal("3.7")),
            (Decimal("67.0"), MonthEnum.Set, Decimal("12.5")),
            (Decimal("67.0"), MonthEnum.Out, Decimal("24.9")),
            (Decimal("67.0"), MonthEnum.Nov, Decimal("37.5")),
            (Decimal("67.0"), MonthEnum.Dez, Decimal("44.4")),
        ],
    )
    def test_calculate_solar_radiation(
        self, latitude: Decimal, month: MonthEnum, expected_result: Decimal
    ):
        # When
        result = calculate_solar_radiation(latitude, month)
        # Then
        assert abs(result - expected_result) <= self.error
