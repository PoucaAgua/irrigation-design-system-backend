from fastapi import APIRouter

from apps.ITN.ITN_service import FlService
from apps.ITN.ITN_service import ITNService
from apps.ITN.ITN_service import ITNService2
from core.domain.entity.itn_entity import FlProjectionInputEntity
from core.domain.entity.itn_entity import ITNProjectionInputEntity
from core.domain.entity.itn_entity import ITNProjectionInputEntity2
from infrastructure.api.v1.responses.itn import ITNResponse

router = APIRouter()

@router.post("/FL", response_model=ITNResponse)
def fl(fl_entity: FlProjectionInputEntity):
    fl = FlService.calc_fl(fl_entity)
    return ITNResponse(value=fl)

@router.post("/ITN", response_model=ITNResponse)
def itn(itn_entity: ITNProjectionInputEntity):
    itn = ITNService.calc_itn(itn_entity)
    return ITNResponse(value=itn)

@router.post("/ITN2", response_model=ITNResponse)
def itn(itn_entity: ITNProjectionInputEntity2):
    itn = ITNService2.calc_itn(itn_entity)
    return ITNResponse(value=itn)