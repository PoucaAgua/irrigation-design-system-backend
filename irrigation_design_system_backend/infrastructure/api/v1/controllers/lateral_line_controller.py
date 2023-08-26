from core.domain.entity.lateral_line_entity import LateralLineEntity
from apps.calculate_lateral_line.calculate_lateral_line import LateralLineService
from infrastructure.api.v1.responses.lateral_line import LateralLineResponse

from fastapi import APIRouter

router = APIRouter()

@router.post("/lateral_line", response_model=LateralLineResponse)

def lateral_line(lateral_line_entity: LateralLineEntity):

    lateral = LateralLineService.calculate_lateral_line(lateral_line_entity)
    return LateralLineResponse(value=lateral)