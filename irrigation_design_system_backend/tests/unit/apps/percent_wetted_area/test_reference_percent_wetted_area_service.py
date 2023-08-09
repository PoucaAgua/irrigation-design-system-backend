from _decimal import Decimal
from core.constants.math import MathConstants
from apps.percent_wetted_area.percent_wetted_area_service import PercentWettedAreaService
from core.domain.entity.percent_wetted_area_entity import (
    IrrigationTreeEntity,
    SaturatedWetRadiusX2Entity,
    ContinuousStripEntity
)


class TestPercentWettedAreaService:
    error = Decimal("1e-2")

    def test_calculate_irrigation_by_tree(self):
        # Given
        input_entity = IrrigationTreeEntity(
            drippers_number=Decimal(4),
            space_between_lines=Decimal(2),
            space_between_plants=Decimal(1.5),
            z=Decimal(0.6),
            q=Decimal(0.02),
            hydraulic_conductivity_of_saturated_soil=Decimal(10)
        )
        dw_expected = PercentWettedAreaService._dw_calculate(input_entity)
        expected_result = Decimal(
            input_entity.drippers_number * MathConstants.PI * dw_expected ** 2 * 100 /
            (4 * input_entity.space_between_plants * input_entity.space_between_lines)
        )

        # When
        result = PercentWettedAreaService.calculate_irrigation_by_tree(input_entity)
        print(result)

        # Then
        assert abs(result - expected_result) <= self.error

    def test_calculate_twice_saturated_wetted_radius(self):
        # Given
        input_entity = SaturatedWetRadiusX2Entity(
            parameter_model_unsaturated_hydraulic=Decimal(2),
            hydraulic_conductivity_of_saturated_soil=Decimal(10),
            q=Decimal(0.02)
        )
        expected_result = Decimal(2) * ((4 / input_entity.parameter_model_unsaturated_hydraulic ** 2 * MathConstants.PI ** 2) +
                                        (input_entity.q / MathConstants.PI * input_entity.hydraulic_conductivity_of_saturated_soil) -
                                        (2 / input_entity.parameter_model_unsaturated_hydraulic * MathConstants.PI)) ** Decimal('0.5')

        # When
        result = PercentWettedAreaService.calculate_twice_saturated_wetted_radius(input_entity)
        print(result)

        # Then
        assert abs(result - expected_result) <= self.error

    def test_calculate_continuous_strip(self):
        # Given
        input_entity = ContinuousStripEntity(
            space_between_plants=Decimal(1.5),
            wetted_zone=Decimal(0.8),
            row_spacing_plants=Decimal(2)
        )
        moistened_area_expected = PercentWettedAreaService()._moistened_area_calculate(input_entity)
        area_occupied_plant_expected = PercentWettedAreaService()._area_occupied_plant_calculate(input_entity)
        expected_result = Decimal(moistened_area_expected / area_occupied_plant_expected * 100)

        # When
        result = PercentWettedAreaService.calculate_continuous_strip(input_entity)
        print(result)

        # Then
        assert abs(result - expected_result) <= self.error


