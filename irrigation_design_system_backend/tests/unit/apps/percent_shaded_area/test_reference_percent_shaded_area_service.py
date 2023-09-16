from _decimal import Decimal

from apps.percent_shaded_area.percent_shaded_area_service import PercentShadedAreaService
from core.domain.entity.percent_shaded_area_entity import (
    PlantCanopyProjectionInputEntity,
    PlantStripProjectionInputEntity,
)


class TestPercentShadedAreaService:
    error = Decimal("1e-2")

    def test_calculate_by_plant_canopy_projection(self):
        # Given
        input_entity = PlantCanopyProjectionInputEntity(
            diameter_projection=Decimal(7),
            space_between_plants=Decimal(1.5),
            space_between_rows=Decimal(2),
        )
        expected_result = Decimal(12.82)

        # When
        result = PercentShadedAreaService.calculate_by_plant_canopy_projection(input_entity)
        print(result)

        # Then
        assert abs(result - expected_result) <= self.error

    def test_calculate_by_plant_strip_projection(self):
        # Given
        input_entity = PlantStripProjectionInputEntity(
            shaded_strip_plant=Decimal(4), space_between_rows=Decimal(2)
        )
        expected_result = Decimal(2)

        # When
        result = PercentShadedAreaService.calculate_by_plant_strip_projection(input_entity)
        print(result)

        # Then
        assert abs(result - expected_result) <= self.error
