from _decimal import Decimal

import numpy as np

from core.domain.entity.uniformity_and_flow_input import FlowRateIrrigationInput
from core.domain.entity.uniformity_and_flow_input import UniformityIrrigationInput

class UniformityAndFlowService:
    @classmethod
    def calculate_flow(
            cls, input_entity: FlowRateIrrigationInput
    ) -> Decimal:
        v1 = input_entity.v1
        v2 = input_entity.v2
        v3 = input_entity.v3
        v4 = input_entity.v4
        v5 = input_entity.v5
        v6 = input_entity.v6
        v7 = input_entity.v7
        v8 = input_entity.v8
        v9 = input_entity.v9
        v10 = input_entity.v10
        v11 = input_entity.v11
        v12 = input_entity.v12
        v13 = input_entity.v13
        v14 = input_entity.v14
        v15 = input_entity.v15
        v16 = input_entity.v16
        time_c = input_entity.time_c
        volume = np.array([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16])
        return Decimal(((np.mean(volume)/1000)/time_c)*60)
    @classmethod
    def calculate_uniformity(
            cls, input_entity: UniformityIrrigationInput
    ) -> Decimal:
        v1 = input_entity.v1
        v2 = input_entity.v2
        v3 = input_entity.v3
        v4 = input_entity.v4
        v5 = input_entity.v5
        v6 = input_entity.v6
        v7 = input_entity.v7
        v8 = input_entity.v8
        v9 = input_entity.v9
        v10 = input_entity.v10
        v11 = input_entity.v11
        v12 = input_entity.v12
        v13 = input_entity.v13
        v14 = input_entity.v14
        v15 = input_entity.v15
        v16 = input_entity.v16
        volume = np.array([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16])
        return Decimal((1 - np.std(volume)/np.mean(volume))*100)
