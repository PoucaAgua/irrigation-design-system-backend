from _decimal import Decimal

from apps.evapotranspiration.reference_evapotranspiration_service import ReferenceEvapotranspirationService
from core.domain.entity.evapotranspiration_entity import EToHargravesSamaniInputyEntity


class TestReferenceEvapotranspirationService:
    error = Decimal("1e-2")

    def test_calculate_hargraves_samani(self):
        # Given
        test_eto_entity = EToHargravesSamaniInputyEntity(
            temperature_med=Decimal(25.0),
            temperature_min=Decimal(20.0),
            temperature_max=Decimal(30.0),
            latitude=Decimal(30.0),
            month= "Jan"
                        

        )
        expected_result = Decimal(2.83)

        # When
        result = ReferenceEvapotranspirationService.calculate_hargraves_samani(test_eto_entity)
        print(result)

        # Then
        assert abs(result - expected_result) <= self.error

    
