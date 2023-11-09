import pytest
from decimal import Decimal

from core.domain.entity.evapotranspiration.temperature_med import calculate_temperature_med


class TestCalculateTemperatureMed:
    def test_temperature_med_provided(self):
        temperature_med = Decimal("25.0")
        result = calculate_temperature_med(temperature_med=temperature_med)
        assert result == temperature_med

    def test_temperature_max_and_min_provided(self):
        temperature_max = Decimal("30.0")
        temperature_min = Decimal("20.0")
        result = calculate_temperature_med(
            temperature_max=temperature_max, temperature_min=temperature_min
        )
        expected_result = (temperature_max + temperature_min) / 2
        assert result == expected_result

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            calculate_temperature_med()

    def test_both_temperature_med_and_max_min_provided(self):
        temperature_med = Decimal("25.0")
        temperature_max = Decimal("30.0")
        temperature_min = Decimal("20.0")
        result = calculate_temperature_med(
            temperature_med=temperature_med,
            temperature_max=temperature_max,
            temperature_min=temperature_min,
        )
        assert result == temperature_med
