from fastapi import APIRouter

from infrastructure.api.v1.responses.derivationline import DerivationlineReponse
from core.domain.entity.derivationline_entity import DerivationlineEntity
from apps.hydraulic_design.derivationline.derivationline_calculate_service import DerivationlineService


router = APIRouter()

@router.post("/derivation_line", response_model=DerivationlineReponse)
def derivationline(derivationline_entity: DerivationlineEntity):

    derivation = DerivationlineService.calculate_derivationline_dimensions(derivationline_entity)
    return DerivationlineReponse(value=derivation)
