from fastapi import APIRouter

from apps.irrigation.total_irrigation_service import (
    TotalIrrigationService,
)
from core.domain.entity.irrigation.total_irrigation_input import (
    TotalIrrigationInput,
)
from infrastructure.api.v1.responses.irrigation.total_irrigation import TotalIrrigationResponse

router = APIRouter()


@router.post("/", response_model=TotalIrrigationResponse)
def total_irrigation(
    total_irrigation_input: TotalIrrigationInput,
):
    total_irrigation_response = TotalIrrigationService.calculate(total_irrigation_input)
    return TotalIrrigationResponse(value=total_irrigation_response)
