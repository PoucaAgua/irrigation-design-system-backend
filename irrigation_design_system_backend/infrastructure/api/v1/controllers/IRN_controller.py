from fastapi import APIRouter

from apps.IRN.IRN_service import IRNSoloService, IRNmaxService, IRNatmService
from core.domain.entity.irn_solo_entity import IRNsoloProjectionInputEntity
from core.domain.entity.irn_solo_entity import IRNatmProjectionInputEntity
from core.domain.entity.irn_solo_entity import IRNmaxProjectionInputEntity
from infrastructure.api.v1.responses.irn import IRNResponse

router = APIRouter()


@router.post("/solo", response_model=IRNResponse)
def irn_solo(irn_entity: IRNsoloProjectionInputEntity):
    irn_solo = IRNSoloService.calc_irn_solo(irn_entity)
    return IRNResponse(value=irn_solo)

@router.post(path="/atm", response_model=IRNResponse)
def irn_atm(irn_entity: IRNatmProjectionInputEntity):
    irn_atm = IRNatmService.calc_irn_atm(irn_entity)
    return IRNResponse(value=irn_atm)

@router.post(path='/IRN_max', response_model=IRNResponse)
def irn_max(irn_entity: IRNmaxProjectionInputEntity):
    irn_max = IRNmaxService.calc_irn_max(irn_entity)
    return IRNResponse(value=irn_max)


