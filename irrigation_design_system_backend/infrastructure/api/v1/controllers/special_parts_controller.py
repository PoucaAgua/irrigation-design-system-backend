from fastapi import APIRouter

from apps.hydraulic_design.special_parts.special_parts_service import SpecialPartsService
from core.domain.entity.special_parts_entity import SpecialPartsEntity
from infrastructure.api.v1.responses.special_parts import SpecialPartsReponse


router = APIRouter()

@router.post("/special_parts")
def percent_wetted_area_irrigation_by_tree(input: SpecialPartsEntity):
    specialparts = SpecialPartsService.special_parts_loadloss(input)
    return SpecialPartsReponse(value=specialparts)
