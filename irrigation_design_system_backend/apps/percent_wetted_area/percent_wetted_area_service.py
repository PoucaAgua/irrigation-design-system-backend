from _decimal import Decimal
from core.constants.math import MathConstants
from core.domain.entity.percent_wetted_area_entity import (
    IrrigationTreeEntity,
    SaturatedWetRadiusX2Entity,
    ContinuousStripEntity,
)


class PercentWettedAreaService:
    @classmethod
    def calculate_irrigation_by_tree(cls, input_entity: IrrigationTreeEntity) -> Decimal:
        Np = input_entity.drippers_number
        Dw = cls._dw_calculate(input_entity)
        Sr = input_entity.space_between_lines
        Sp = input_entity.space_between_plants
        return Decimal(Np * MathConstants.PI * Dw**2 * 100 / (4 * Sp * Sr))

    @classmethod
    def _dw_calculate(cls, input_entity: IrrigationTreeEntity) -> Decimal:
        Z = input_entity.z
        q = input_entity.q
        K0 = input_entity.hydraulic_conductivity_of_saturated_soil
        return Decimal("1.32") * Z ** Decimal("0.35") * (q / K0) ** Decimal("0.33")

    @classmethod
    def calculate_twice_saturated_wetted_radius(
        cls, input_entity: SaturatedWetRadiusX2Entity
    ) -> Decimal:
        alpha = input_entity.parameter_model_unsaturated_hydraulic
        k0 = input_entity.hydraulic_conductivity_of_saturated_soil
        q = input_entity.q

        part1 = 2 / (alpha * MathConstants.PI)
        part2 = q / (MathConstants.PI * k0)
        result = Decimal(2) * ((part1**2 + part2) ** Decimal("0.5") - part1)
        return result

    @classmethod
    def calculate_continuous_strip(cls, input_entity: ContinuousStripEntity) -> Decimal:
        Aw = cls._moistened_area_calculate(input_entity)
        Ap = cls._area_occupied_plant_calculate(input_entity)
        return Decimal(Aw / Ap * 100)

    @classmethod
    def _moistened_area_calculate(cls, input_entity: ContinuousStripEntity) -> Decimal:
        Sp = input_entity.space_between_plants
        Sw = input_entity.wetted_zone
        return Sp * Sw

    @classmethod
    def _area_occupied_plant_calculate(cls, input_entity: ContinuousStripEntity) -> Decimal:
        Sp = input_entity.space_between_plants
        Sr = input_entity.row_spacing_plants
        return Sp * Sr
