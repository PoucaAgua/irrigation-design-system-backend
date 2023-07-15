from fastapi import APIRouter

from apps.evapotranspiration.reference_evapotranspiration_service import ReferenceEvapotranspirationService
from core.domain.entity.evapotranspiration_entity import EToEntity
from infrastructure.api.v1.responses.evapotranspiration import EvapotranspirationResponse

router = APIRouter()


@router.post("/hargraves_samani", response_model=EvapotranspirationResponse)
def evapotranspiration(eto_entity: EToEntity):
    eto = ReferenceEvapotranspirationService.calculate_hargraves_samani(eto_entity)
    return EvapotranspirationResponse(value=eto)
