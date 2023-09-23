from fastapi import APIRouter

from apps.irrigation.total_irrigation.total_irrigation_service import (
    TotalIrrigationService,
)
from core.domain.entity.total_irrigation_input import TotalIrrigationByLixiviationFractionInput
from core.domain.entity.total_irrigation_input import TotalIrrigationByElectricalConductivityInput
from infrastructure.api.v1.responses.total_irrigation import TotalIrrigationResponse

router = APIRouter()


@router.post("/lixiviation_fraction", response_model=TotalIrrigationResponse)
def total_irrigation_by_lixiviation_fraction(
    total_irrigation_input: TotalIrrigationByLixiviationFractionInput,
):
    total_irrigation = TotalIrrigationService.calculate_by_lixiviation_fraction(
        total_irrigation_input
    )
    return TotalIrrigationResponse(value=total_irrigation)


@router.post("/electrical_conductivity", response_model=TotalIrrigationResponse)
def total_irrigation_by_electrical_conductivity(
    total_irrigation_input: TotalIrrigationByElectricalConductivityInput,
):
    total_irrigation = TotalIrrigationService.calculate_by_electrical_conductivity(
        total_irrigation_input
    )
    return TotalIrrigationResponse(value=total_irrigation)
