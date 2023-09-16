from fastapi import APIRouter, HTTPException, status

from infrastructure.api.v1.responses.derivationline import (
    DerivationLineDiameterResponse,
    DerivationLineLoadLossResponse
)
from core.domain.entity.derivation_line_input import DerivationLineLoadLossInput, DerivationLineDiameterInput
from apps.hydraulic_design.derivationline.derivationline_calculate_service import DerivationLineService

router = APIRouter()


@router.post("/diameter", response_model=DerivationLineDiameterResponse)
def derivation_line_diameter(input_entity: DerivationLineDiameterInput):
    try:
        derivation = DerivationLineService.calculate_diameter(input_entity)
        return DerivationLineDiameterResponse(value=derivation)
    except KeyError as k:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(k))


@router.post("/load_loss", response_model=DerivationLineLoadLossResponse)
def derivation_line_load_loss(input_entity: DerivationLineLoadLossInput):
    load_loss = DerivationLineService.calculate_load_loss(input_entity)
    return DerivationLineLoadLossResponse(value=load_loss)
