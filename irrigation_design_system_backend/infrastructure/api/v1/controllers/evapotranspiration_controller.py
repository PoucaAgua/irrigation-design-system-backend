from fastapi import APIRouter

from apps.evapotranspiration.reference_evapotranspiration.reference_evapotranspiration_service import (
    ReferenceEvapotranspirationService,
)
from core.domain.entity.evapotranspiration_input import (
    EToHargreavesSamaniInput,
    EToPenmanMonteithInputyEntity,
    EToBlanneyCriddleInputy,
)
from infrastructure.api.v1.responses.evapotranspiration import EvapotranspirationResponse

router = APIRouter()


@router.post("/hargreaves_samani", response_model=EvapotranspirationResponse)
def evapotranspiration_hargreaves_samani(eto_input: EToHargreavesSamaniInput):
    eto = ReferenceEvapotranspirationService.calculate_hargreaves_samani(eto_input)
    return EvapotranspirationResponse(value=eto)


@router.post("/blaney_criddle", response_model=EvapotranspirationResponse)
def evapotranspiration_blaney_criddle(eto_entity: EToBlanneyCriddleInputy):
    eto = ReferenceEvapotranspirationService.calculate_blaney_criddle(eto_entity)
    return EvapotranspirationResponse(value=eto)


@router.post("/penman_monteith", response_model=EvapotranspirationResponse)
def evapotranspiration_penman_monteith(eto_entity: EToPenmanMonteithInputyEntity):
    eto = ReferenceEvapotranspirationService.calculate_penman_monteith(eto_entity)
    return EvapotranspirationResponse(value=eto)
