from _decimal import Decimal
from core.constants.math import MathConstants
from core.domain.entity.percent_shaded_area_entity import (
    PlantCanopyProjectionInputEntity,
    PlantStripProjectionInputEntity
)


class PercentShadedAreaService:

    @classmethod
    def calculate_by_plant_canopy_projection(cls, input_entity: PlantCanopyProjectionInputEntity) -> Decimal:
        Dco = input_entity.diameter_projection
        Sp = input_entity.space_between_plants
        Sr = input_entity.space_between_rows
        return Decimal(MathConstants.PI * (Dco ** 2 / 4) / (Sr * Sp))

    @classmethod
    def calculate_by_plant_strip_projection(cls, input_entity: PlantStripProjectionInputEntity) -> Decimal:
        Ss = input_entity.shaded_strip_plant
        Sr = input_entity.space_between_rows
        return Decimal(Ss / Sr)
