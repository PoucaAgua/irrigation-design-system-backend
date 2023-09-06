from fastapi import APIRouter

from infrastructure.api.v1.responses.derivationline import DerivationlineDiameterReponse,  DerivationlineLoadLossReponse
from core.domain.entity.derivationline_entity import DerivationlineLoadLoassEntity, DerivationlineDiameterEntity
from apps.hydraulic_design.derivationline.derivationline_calculate_service import DerivationlineService



router = APIRouter()

@router.post("/derivationline_diameter", response_model=DerivationlineDiameterReponse)
def derivationline_diameter(input_entity: DerivationlineDiameterEntity):
    derivation = DerivationlineService.calculate_derivationline_dimensions(input_entity)
    return DerivationlineDiameterReponse(value=derivation)

@router.post("/derivationline_loadloss", response_model=DerivationlineLoadLossReponse)
def derivationline_loadloss(input_entity: DerivationlineLoadLoassEntity):
    loadloss = DerivationlineService.calculate_loadloass_derivationline(input_entity)
    return DerivationlineLoadLossReponse(value=loadloss)
