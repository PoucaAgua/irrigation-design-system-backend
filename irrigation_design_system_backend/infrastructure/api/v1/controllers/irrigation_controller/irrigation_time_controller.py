from fastapi import APIRouter

from apps.irrigation.irrigation_time_service import IrrigationTimeService

from core.domain.entity.irrigation.irrigation_time_input import (
    IrrigationTimeByPlantInput,
    IrrigationTimeByLineInput,
)

from infrastructure.api.v1.responses.irrigation.irrigation_time import IrrigationTimeResponse

router = APIRouter()


@router.post("/plant", response_model=IrrigationTimeResponse)
def irrigation_time_by_plant(irrigation_time_input: IrrigationTimeByPlantInput):
    irrigation_time_response = IrrigationTimeService.calculate_by_plant_params(
        irrigation_time_input
    )
    return IrrigationTimeResponse(value=irrigation_time_response)


@router.post("/line", response_model=IrrigationTimeResponse)
def irrigation_time_by_line(irrigation_time_input: IrrigationTimeByLineInput):
    irrigation_time_response = IrrigationTimeService.calculate_by_line_params(irrigation_time_input)
    return IrrigationTimeResponse(value=irrigation_time_response)
