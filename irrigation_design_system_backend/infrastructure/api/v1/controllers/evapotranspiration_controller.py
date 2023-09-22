from fastapi import APIRouter

from apps.evapotranspiration.reference_evapotranspiration.reference_evapotranspiration_service import (
    ReferenceEvapotranspirationService,
)
from core.domain.entity.evapotranspiration_input import (
    EToHargravesSamaniInput,
    EToPenmanMonteithInput,
    EToBlanneyCriddleInput,
)
from infrastructure.api.v1.responses.evapotranspiration import EvapotranspirationResponse

router = APIRouter()


@router.post("/hargraves_samani", response_model=EvapotranspirationResponse)
def evapotranspiration_hargraves_samani(eto_input: EToHargravesSamaniInput):
    eto = ReferenceEvapotranspirationService.calculate_by_hargraves_samani(eto_input)
    return EvapotranspirationResponse(value=eto)


@router.post("/blaney_criddle", response_model=EvapotranspirationResponse)
def evapotranspiration_blaney_criddle(eto_entity: EToBlanneyCriddleInput):
    eto = ReferenceEvapotranspirationService.calculate_by_blaney_criddle(eto_entity)
    return EvapotranspirationResponse(value=eto)


@router.post("/penman_monteith", response_model=EvapotranspirationResponse)
def evapotranspiration_penman_monteith(eto_entity: EToPenmanMonteithInput):
    eto = ReferenceEvapotranspirationService.calculate_penman_monteith(eto_entity)
    return EvapotranspirationResponse(value=eto)
