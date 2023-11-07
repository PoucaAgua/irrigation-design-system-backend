from fastapi import APIRouter, HTTPException, status

from infrastructure.api.v1.responses.lateral_line import (
    LateralLineDiameterResponse,
    LateralLineHeadLossResponse,
)
from core.domain.entity.lateral_line_entity import (
    LateralLineInput,
    LateralLineHeadLossInput
)
from apps.hydraulic_design.calculate_lateral_line.calculate_lateral_line import (
    LateralLineService,
)

router = APIRouter()


@router.post("/diameter", response_model=LateralLineDiameterResponse)
def lateral_line_diameter(input_entity: LateralLineInput):
    try:
        lateral_line = LateralLineService.calculate_length_lateral_line(input_entity)
        return LateralLineDiameterResponse(value=lateral_line)
    except KeyError as k:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(k))


@router.post("/head_loss", response_model=LateralLineDiameterResponse)
def lateral_line_load_loss(input_entity: LateralLineHeadLossInput):
    load_loss = LateralLineService.calculate_head_loss(input_entity)
    return LateralLineHeadLossResponse(value=load_loss)
