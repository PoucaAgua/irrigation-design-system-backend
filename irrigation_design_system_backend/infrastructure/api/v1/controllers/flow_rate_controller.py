from fastapi import APIRouter

from apps.uniformity_and_flow.uniformty_and_flow_service import UniformityAndFlowService

from core.domain.entity.uniformity_and_flow_input import FlowRateIrrigationInput

from infrastructure.api.v1.responses.flow_rate import FlowRateResponse

router = APIRouter()


@router.post("/", response_model=FlowRateResponse)
def flow_irrigation(flow_input: FlowRateIrrigationInput):
    flow_responde = UniformityAndFlowService.calculate_flow(flow_input)
    return FlowRateResponse(value=flow_responde)
