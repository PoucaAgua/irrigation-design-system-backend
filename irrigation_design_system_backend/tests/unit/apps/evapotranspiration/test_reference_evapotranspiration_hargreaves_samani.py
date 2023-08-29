from _decimal import Decimal

import pytest

from apps.evapotranspiration.funcitions_to_reference_evapotranspiration import calculate_radiation_hargreaves_samani
from apps.evapotranspiration.reference_evapotranspiration_service import ReferenceEvapotranspirationService
from core.domain.entity.evapotranspiration_entity import EToHargravesSamaniInputyEntity
from core.domain.enum.month import MonthEnum


class TestReferenceEvapotranspirationHargreavesSamani:
    error = Decimal("1e-2")

    @pytest.mark.parametrize(
        "latitude, month, expected_result",
        [
            (Decimal("69.0"), MonthEnum.Jan, Decimal("41.2")),  # Add more test cases here
            (Decimal("69.0"), MonthEnum.Fev, Decimal("28.95")),  # Add more test cases here
            # (latitude, month, expected_result),
            # ...
        ]
    )
    def test_calculate_radiation_hargreaves_samani(
            self,
            latitude: Decimal,
            month: MonthEnum,
            expected_result: Decimal
    ):

        # When
        result = calculate_radiation_hargreaves_samani(latitude, month)
        print(result)
        # Then
        assert abs(result - expected_result) <= self.error

    
