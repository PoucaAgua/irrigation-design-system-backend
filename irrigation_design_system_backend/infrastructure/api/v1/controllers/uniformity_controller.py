from fastapi import APIRouter

from apps.uniformity_and_flow.uniformty_and_flow_service import UniformityAndFlowService

from core.domain.entity.uniformity_and_flow_input import UniformityIrrigationInput

from infrastructure.api.v1.responses.uniformity import UniformityResponse

router = APIRouter()

@router.post("/", response_model=UniformityResponse)
def uniformity_irrigation(uniformity_input: UniformityIrrigationInput):
    uniformity_responde = UniformityAndFlowService.calculate_uniformity(uniformity_input)
    return UniformityResponse(value=uniformity_responde)
