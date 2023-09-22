from fastapi import APIRouter

from apps.IRN.IRN_service import IrrigationRealNecessaryService
from core.domain.entity.irn_solo_entity import IRNatmInputEntity
from core.domain.entity.irn_solo_entity import IRNsoilInputEntity
from core.domain.entity.irn_solo_entity import IRNmaxInputEntity
from infrastructure.api.v1.responses.irn import IRNResponse

router = APIRouter()


@router.post("/IRN_solo", response_model=IRNResponse)
def irn(irn_entity: IRNsoilInputEntity):
    irn = IrrigationRealNecessaryService.calc_irn_solo(irn_entity)
    return IRNResponse(value=irn)

@router.post(path="/IRN_atm", response_model=IRNResponse)
def irn(irn_entity: IRNatmInputEntity):
    irn = IrrigationRealNecessaryService.calc_irn_atm(irn_entity)
    return IRNResponse(value=irn)

@router.post(path='/IRN_max', response_model=IRNResponse)
def irn(irn_entity: IRNmaxInputEntity):
    irn = IrrigationRealNecessaryService.calc_irn_max(irn_entity)
    return IRNResponse(value=irn)
