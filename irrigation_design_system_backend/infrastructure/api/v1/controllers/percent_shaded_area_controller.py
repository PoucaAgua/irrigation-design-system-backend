from fastapi import APIRouter
from apps.percent_shaded_area.percent_shaded_area_service import PercentShadedAreaService
from core.domain.entity.PSAEntity import SAEntity,CPEntity
from infrastructure.api.v1.responses.percent_shaded_area import SAResponse,CPResponse

router = APIRouter()

@router.post("/shaded_area")
def percent_shaded_area(sa_entity: SAEntity):
    Sa = PercentShadedAreaService.calculate_shaded_area(sa_entity)
    return SAResponse(value=Sa)

@router.post("/shaded_area_crop_projection")
def percent_shaded_area_crop_projection(cp_entity: CPEntity):
    Cp = PercentShadedAreaService.calculate_crop_projection(cp_entity)
    return CPResponse(value=Cp)