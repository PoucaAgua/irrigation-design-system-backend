from fastapi import APIRouter

from apps.irrigation.maximum_irrigation_shift_service import MaximumIrrigationShiftService
from apps.irrigation.total_irrigation_service import (
    TotalIrrigationService,
)
from core.domain.entity.irrigation.maximum_irrigation_shift_input import MaximumIrrigationShiftInput
from core.domain.entity.irrigation.total_irrigation_input import (
    TotalIrrigationInput,
)
from infrastructure.api.v1.responses.irrigation.maximum_irrigation_shift import (
    MaximumIrrigationShiftResponse,
)
from infrastructure.api.v1.responses.irrigation.total_irrigation import TotalIrrigationResponse

router = APIRouter()


@router.post("/", response_model=MaximumIrrigationShiftResponse)
def maximum_irrigation_shift(
    maximum_irrigation_shift_input: MaximumIrrigationShiftInput,
):
    maximum_irrigation_shift_response = MaximumIrrigationShiftService.calculate(
        maximum_irrigation_shift_input
    )
    return MaximumIrrigationShiftResponse(value=maximum_irrigation_shift_response)
