from fastapi import APIRouter

from apps.irrigation.actual_irrigation.actual_irrigation_service import (
    ActualIrrigationNecessaryService,
)
from core.domain.entity.actual_irrigation_input import ActualIrrigationByAtmosphericParamsInput
from core.domain.entity.actual_irrigation_input import ActualIrrigationBySoilParamsInput
from core.domain.entity.actual_irrigation_input import IRNmaxInputEntity
from infrastructure.api.v1.responses.actual_irrigation import IRNResponse

router = APIRouter()


@router.post("/IRN_solo", response_model=IRNResponse)
def irn(irn_entity: ActualIrrigationBySoilParamsInput):
    irn = ActualIrrigationNecessaryService.calculate_by_soil_params(irn_entity)
    return IRNResponse(value=irn)


@router.post(path="/IRN_atm", response_model=IRNResponse)
def irn(irn_entity: ActualIrrigationByAtmosphericParamsInput):
    irn = ActualIrrigationNecessaryService.calculate_by_atmospheric_params(irn_entity)
    return IRNResponse(value=irn)


@router.post(path="/IRN_max", response_model=IRNResponse)
def irn(irn_entity: IRNmaxInputEntity):
    irn = ActualIrrigationNecessaryService.calculate_max_actual_irrigation(irn_entity)
    return IRNResponse(value=irn)
