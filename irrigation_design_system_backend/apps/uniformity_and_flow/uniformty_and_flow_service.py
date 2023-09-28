from _decimal import Decimal

import numpy as np

from core.domain.entity.uniformity_and_flow_input import (
    FlowRateIrrigationInput,
    UniformityIrrigationInput,
)

class UniformityAndFlowService:
    @classmethod
    def calculate_flow(cls, input_entity: FlowRateIrrigationInput) -> Decimal:
        volume = np.array(input_entity.volume_collected_points)
        time = input_entity.time
        result = ((np.mean(volume) / 1000) / time) * 60
        return Decimal(f"{result:.2f}")

    @classmethod
    def calculate_uniformity(cls, input_entity: UniformityIrrigationInput) -> Decimal:
        volume = np.array(input_entity.volume_collected_points)
        result = ((1 - np.std(volume) / np.mean(volume)) * 100)
        return Decimal(f"{result:.2f}")