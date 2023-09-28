from typing import List

from pydantic import BaseModel, Field


class UniformityIrrigationInput(BaseModel):
    volume_collected_points: List[int]


class FlowRateIrrigationInput(UniformityIrrigationInput):
    time: float = Field(..., ge=0, description="[Time] Time for water collection (minutes)")
