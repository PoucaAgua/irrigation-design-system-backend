from _decimal import Decimal

from core.domain.entity.irrigation.irrigation_time_input import (
    IrrigationTimeByPlantInput,
    IrrigationTimeByLineInput,
)


class IrrigationTimeService:
    @classmethod
    def calculate_by_plant_params(cls, input_entity: IrrigationTimeByPlantInput) -> Decimal:
        itn = input_entity.total_irrigation
        sp = input_entity.spacing_between_plants
        sl = input_entity.spacing_between_side_lines
        ne = input_entity.number_of_emitters_per_plant
        q = input_entity.emitter_flow
        result = (itn * sp * sl) / (ne * q)
        return Decimal(f"{result:.2f}")

    @classmethod
    def calculate_by_line_params(cls, input_entity: IrrigationTimeByLineInput) -> Decimal:
        itn = input_entity.total_irrigation
        se = input_entity.spacing_between_emitters
        sl = input_entity.spacing_between_side_lines
        q = input_entity.emitter_flow
        result = (itn * se * sl) / q
        return Decimal(f"{result:.2f}")
