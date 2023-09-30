from fastapi import APIRouter

from apps.irrigation.maximum_irrigation_shift_service import MaximumIrrigationShiftService
from core.domain.entity.irrigation.maximum_irrigation_shift_input import MaximumIrrigationShiftInput
from infrastructure.api.v1.responses.irrigation.maximum_irrigation_shift import (
    MaximumIrrigationShiftResponse,
)

router = APIRouter()


@router.post("/", response_model=MaximumIrrigationShiftResponse)
def maximum_irrigation_shift(
    maximum_irrigation_shift_input: MaximumIrrigationShiftInput,
):
    maximum_irrigation_shift_response = MaximumIrrigationShiftService.calculate(
        maximum_irrigation_shift_input
    )
    return MaximumIrrigationShiftResponse(value=maximum_irrigation_shift_response)
