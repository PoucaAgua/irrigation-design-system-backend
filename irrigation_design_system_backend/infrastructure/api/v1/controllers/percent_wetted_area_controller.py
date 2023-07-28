from fastapi import APIRouter

from apps.percent_wetted_area.percent_wetted_area_service import PercentWettedAreaService
from core.domain.entity.PWAEntity import PWAEntity
from infrastructure.api.v1.responses.percent_wetted_area import PWAResponse

router = APIRouter()


@router.post("/")
def percent_wetted_area(pwa_entity: PWAEntity):
    Pwa = PercentWettedAreaService.calculate(pwa_entity)
    return PWAResponse(value=Pwa)
