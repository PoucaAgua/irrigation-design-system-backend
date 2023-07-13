from fastapi import APIRouter

from apps.evapotranspiration.reference_evapotranspiration import ReferenceEvapotranspiration
from core.domain.entity.evapotranspiration import EToData
from infrastructure.api.v1.responses.evapotranspiration import EvapotranspirationResponse

router = APIRouter()


@router.post("/hargraves_samani", response_model=EvapotranspirationResponse)
def evapotranspiration(data: EToData):
    eto_data = data
    eto = ReferenceEvapotranspiration.calculate_hargraves_samani(eto_data)
    return EvapotranspirationResponse(value=eto)
