from fastapi import APIRouter

from apps.hydraulic_design.special_parts.special_parts_service import SpecialPartsService
from core.domain.entity.special_parts_input import SpecialPartsInput
from infrastructure.api.v1.responses.special_parts import SpecialPartsReponse

router = APIRouter()


@router.post("/load_loss")
def special_parts_load_loss(input: SpecialPartsInput):
    special_parts = SpecialPartsService.special_parts_load_loss(input)
    return SpecialPartsReponse(value=special_parts)
