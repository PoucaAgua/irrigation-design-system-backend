from fastapi import APIRouter

from apps.evapotranspiration.reference_evapotranspiration_service import ReferenceEvapotranspirationService
from core.domain.entity.evapotranspiration_entity import EToHargravesSamaniInputyEntity, EToPenmanMonteithInputyEntity, EToBlanneyCriddleInputyEntity
from infrastructure.api.v1.responses.evapotranspiration import EvapotranspirationResponse

router = APIRouter()


@router.post("/hargraves_samani", response_model=EvapotranspirationResponse)
def evapotranspiration_hargraves_samani(eto_entity: EToHargravesSamaniInputyEntity):
    eto = ReferenceEvapotranspirationService.calculate_hargraves_samani(eto_entity)   
    return EvapotranspirationResponse(value=eto)


@router.post("/blaney_criddle", response_model=EvapotranspirationResponse)
def evapotranspiration_blaney_criddle(eto_entity: EToBlanneyCriddleInputyEntity):
    eto = ReferenceEvapotranspirationService.calculate_blaney_cridlle(eto_entity)   
    return EvapotranspirationResponse(value=eto)


@router.post("/penman_monteith", response_model=EvapotranspirationResponse)
def evapotranspiration_penman_monteith(eto_entity: EToPenmanMonteithInputyEntity):
    eto = ReferenceEvapotranspirationService.calculate_penman_monteith(eto_entity)   
    return EvapotranspirationResponse(value=eto)



