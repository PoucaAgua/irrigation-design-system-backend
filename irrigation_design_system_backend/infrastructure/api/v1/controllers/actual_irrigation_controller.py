from fastapi import APIRouter

from apps.irrigation.actual_irrigation.actual_irrigation_service import (
    ActualIrrigationService,
)
from core.domain.entity.actual_irrigation_input import ActualIrrigationByAtmosphericParamsInput
from core.domain.entity.actual_irrigation_input import ActualIrrigationBySoilParamsInput
from core.domain.entity.actual_irrigation_input import MaxActualIrrigationInput
from infrastructure.api.v1.responses.actual_irrigation import ActualIrrigationResponse

router = APIRouter()


@router.post("/soil_params", response_model=ActualIrrigationResponse)
def actual_irrigation_by_soil_params(actual_irrigation_input: ActualIrrigationBySoilParamsInput):
    actual_irrigation_response = ActualIrrigationService.calculate_by_soil_params(
        actual_irrigation_input
    )
    return ActualIrrigationResponse(value=actual_irrigation_response)


@router.post(path="/atmospheric_params", response_model=ActualIrrigationResponse)
def actual_irrigation_by_atmospheric_params(
    actual_irrigation_input: ActualIrrigationByAtmosphericParamsInput,
):
    actual_irrigation_response = ActualIrrigationService.calculate_by_atmospheric_params(
        actual_irrigation_input
    )
    return ActualIrrigationResponse(value=actual_irrigation_response)


@router.post(path="/maximum", response_model=ActualIrrigationResponse)
def max_actual_irrigation(max_actual_irrigation_input: MaxActualIrrigationInput):
    max_actual_irrigation_response = ActualIrrigationService.calculate_max_actual_irrigation(
        max_actual_irrigation_input
    )
    return ActualIrrigationResponse(value=max_actual_irrigation_response)
