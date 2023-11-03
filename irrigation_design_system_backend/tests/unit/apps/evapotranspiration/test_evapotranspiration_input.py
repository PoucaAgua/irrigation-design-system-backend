from core.domain.entity.reference_evapotranspiration_input import (
    EToHargravesSamaniInput,
    EToBlanneyCriddleInput,
    EToPenmanMonteithInput,
)

import pytest
from decimal import Decimal
from core.domain.enum.hemisphere import Hemisphere
from core.domain.enum.month import MonthEnum


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            EToHargravesSamaniInput(
                temperature_med=Decimal("25.0"), latitude=Decimal("44.0"), month=MonthEnum.Dez
            ),
            EToHargravesSamaniInput(
                temperature_med=Decimal("25.0"), latitude=Decimal("44.0"), month=MonthEnum.Dez
            ),
        ),
        (
            EToBlanneyCriddleInput(
                temperature_med=Decimal("25.0"),
                temperature_max=Decimal("30.0"),
                temperature_min=Decimal("20.0"),
                latitude=44,
                hemisphere=Hemisphere.NORTE,
                month=MonthEnum.Dez,
            ),
            EToBlanneyCriddleInput(
                temperature_med=Decimal("25.0"),
                temperature_max=Decimal("30.0"),
                temperature_min=Decimal("20.0"),
                latitude=44,
                hemisphere=Hemisphere.NORTE,
                month=MonthEnum.Dez,
            ),
        ),
        (
            EToPenmanMonteithInput(
                temperature_med=25.0,
                relative_humidity_air=50.0,
                days=30.0,
                altitude=100.0,
                wind_speed=10.0,
                ground_heat=5.0,
                daily_radiation=20.0,
            ),
            EToPenmanMonteithInput(
                temperature_med=25.0,
                relative_humidity_air=50.0,
                days=30.0,
                altitude=100.0,
                wind_speed=10.0,
                ground_heat=5.0,
                daily_radiation=20.0,
            ),
        ),
    ],
)
def test_etohargravessamani(input_data, expected_output):
    result = EToHargravesSamaniInput.check(input_data)
    assert result == expected_output


def test_etoblanneycriddle(input_data, expected_output):
    result = EToBlanneyCriddleInput.check(input_data)
    assert result == expected_output


def test_etopenmanmonteith(input_data, expected_output):
    result = EToPenmanMonteithInput.check(input_data)
    assert result == expected_output
