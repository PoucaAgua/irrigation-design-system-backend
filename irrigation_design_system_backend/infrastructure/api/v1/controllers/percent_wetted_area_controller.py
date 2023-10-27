from fastapi import APIRouter
from apps.percent_wetted_area.percent_wetted_area_service import (
    PercentWettedAreaService,
)
from infrastructure.api.v1.responses.percent_wetted_area import (
    IrrigationTreeResponse,
    SaturatedWetRadiusX2Response,
    ContinuousStripResponse,
)
from core.domain.entity.percent_wetted_area_entity import (
    IrrigationTreeEntity,
    SaturatedWetRadiusX2Entity,
    ContinuousStripEntity,
)

router = APIRouter()


@router.post("/percent_wetted_area_irrigation_by_tree")
def percent_wetted_area_irrigation_by_tree(input: IrrigationTreeEntity):
    percent_wetted_area = PercentWettedAreaService.calculate_irrigation_by_tree(input)
    return IrrigationTreeResponse(value=percent_wetted_area)


@router.post("/calculate_twice_saturated_wetted_radius")
def calculate_twice_saturated_wetted_radius(input: SaturatedWetRadiusX2Entity):
    percent_wetted_area = PercentWettedAreaService.calculate_twice_saturated_wetted_radius(input)
    return SaturatedWetRadiusX2Response(value=percent_wetted_area)


@router.post("/percent_wetted_area_continuous_strip")
def percent_wetted_area_continuous_strip(input: ContinuousStripEntity):
    percent_wetted_area = PercentWettedAreaService.calculate_continuous_strip(input)
    return ContinuousStripResponse(value=percent_wetted_area)
