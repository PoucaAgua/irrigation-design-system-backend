from fastapi import APIRouter

from apps.ITN.ITN_service import IrrigationTotalNecessaryService
from core.domain.entity.itn_entity import ITNFLInputEntity
from core.domain.entity.itn_entity import ITNCeEntity
from infrastructure.api.v1.responses.itn import ITNResponse

router = APIRouter()

@router.post("/ITN_by_fl", response_model=ITNResponse)
def itn(itn_entity: ITNFLInputEntity):
    itn = IrrigationTotalNecessaryService.calculate_by_fl(itn_entity)
    return ITNResponse(value=itn)

@router.post("/ITN_by_ce", response_model=ITNResponse)
def itn(itn_entity: ITNCeEntity):
    itn = IrrigationTotalNecessaryService.calculate_by_ce(itn_entity)
    return ITNResponse(value=itn)