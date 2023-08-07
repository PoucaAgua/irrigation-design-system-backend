from fastapi import APIRouter
from apps.percent_wetted_area.percent_wetted_area_service import PercentWettedAreaService
from core.domain.entity.PWAEntity import IBTEntity,TSWEntity,CPEntity
from infrastructure.api.v1.responses.percent_wetted_area import IBTResponse,TSWResponse,CPResponse

router = APIRouter()

@router.post("/percent_wetted_area_irrigation_by_tree")
def percent_wetted_area_irrigation_by_tree(ibt_entity: IBTEntity):
    ibt = PercentWettedAreaService.calculate_irrigation_by_tree(ibt_entity)
    return IBTResponse(value=ibt)

@router.post("/percent_wetted_area_continuous_strip")
def percent_wetted_area_continuous_strip(tsw_entity: TSWEntity):
    Tsw = PercentWettedAreaService.calculate_continuous_strip(tsw_entity)
    return TSWResponse(value=Tsw)

@router.post("/calculate_twice_saturated_wetted_radius")
def calculate_twice_saturated_wetted_radius(cp_entity: CPEntity):
    Cp = PercentWettedAreaService.calculate_twice_saturated_wetted_radius(cp_entity)
    return CPResponse(value=Cp)