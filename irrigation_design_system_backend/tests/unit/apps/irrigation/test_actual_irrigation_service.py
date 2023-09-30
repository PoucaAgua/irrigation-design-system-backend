from _decimal import Decimal
import pytest

from apps.irrigation.actual_irrigation_service import ActualIrrigationService
from core.domain.entity.irrigation.actual_irrigation_input import (
    ActualIrrigationBySoilParamsInput,
    MaxActualIrrigationInput,
)


class TestActualIrrigationService:
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                ActualIrrigationBySoilParamsInput(
                    soil_moisture_field_capacity=0.3,
                    soil_moisture_at_permanent_wilting_point=0.1,
                    soil_depth=30,
                    depletion_factor=0.8,
                    effective_precipitation=10,
                ),
                Decimal(38),
            ),
            (
                ActualIrrigationBySoilParamsInput(
                    soil_moisture_field_capacity=0.3,
                    soil_moisture_at_permanent_wilting_point=0.1,
                    soil_depth=30,
                    depletion_factor=0.8,
                ),
                Decimal(48),
            ),
            (
                ActualIrrigationBySoilParamsInput(
                    soil_moisture_field_capacity=0.3,
                    soil_moisture_at_permanent_wilting_point=0.1,
                    soil_depth=30,
                    depletion_factor=0.8,
                    effective_precipitation=70,
                ),
                Decimal(0),
            ),
        ],
    )
    def test_calculate_by_soil_params(
        self, input_data: ActualIrrigationBySoilParamsInput, expected_output: Decimal
    ):
        result = ActualIrrigationService.calculate_by_soil_params(input_data)
        assert result == expected_output

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                MaxActualIrrigationInput(
                    soil_moisture_field_capacity=0.3,
                    soil_moisture_at_permanent_wilting_point=0.1,
                    soil_depth=30,
                    depletion_factor=0.8,
                    effective_precipitation=10,
                    fraction_of_total_wetted_area=0.7,
                ),
                Decimal("26.6"),
            ),
            (
                MaxActualIrrigationInput(
                    soil_moisture_field_capacity=0.3,
                    soil_moisture_at_permanent_wilting_point=0.1,
                    soil_depth=30,
                    depletion_factor=0.8,
                    fraction_of_total_wetted_area=0.7,
                ),
                Decimal("33.6"),
            ),
            (
                MaxActualIrrigationInput(
                    soil_moisture_field_capacity=0.3,
                    soil_moisture_at_permanent_wilting_point=0.1,
                    soil_depth=30,
                    depletion_factor=0.8,
                    effective_precipitation=70,
                    fraction_of_total_wetted_area=0.7,
                ),
                Decimal(0),
            ),
        ],
    )
    def test_calculate_max_actual_irrigation(
        self, input_data: MaxActualIrrigationInput, expected_output: Decimal
    ):
        result = ActualIrrigationService.calculate_max_actual_irrigation(input_data)
        assert result == expected_output
