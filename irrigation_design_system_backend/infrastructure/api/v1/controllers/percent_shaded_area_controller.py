from fastapi import APIRouter
from apps.percent_shaded_area.percent_shaded_area_service import PercentShadedAreaService
from core.domain.entity.percent_shaded_area_entity import (
    PlantStripProjectionInputEntity,
    PlantCanopyProjectionInputEntity,
)
from infrastructure.api.v1.responses.percent_shaded_area import (
    PercentShadedAreaByCanopyResponse,
    PercentShadedAreaByStripResponse,
)

router = APIRouter()


@router.post("/plant_canopy_projection")
def percent_shaded_area_by_plant_canopy_projection(input: PlantCanopyProjectionInputEntity):
    percent_shaded_area = PercentShadedAreaService.calculate_by_plant_canopy_projection(input)
    return PercentShadedAreaByCanopyResponse(value=percent_shaded_area)


@router.post("/plant_strip_projection")
def percent_shaded_area_by_plant_strip_projection(input: PlantStripProjectionInputEntity):
    percent_shaded_area = PercentShadedAreaService.calculate_by_plant_strip_projection(input)
    return PercentShadedAreaByStripResponse(value=percent_shaded_area)
