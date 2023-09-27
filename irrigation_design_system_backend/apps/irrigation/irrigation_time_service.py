from _decimal import Decimal

from core.domain.entity.irrigation.irrigation_time_input import (
    IrrigationTimeByPlantInput,
    IrrigationTimeByLineInput,
)


class IrrigationTimeService:
    @classmethod
    def calculate_by_plant_params(cls, input_entity: IrrigationTimeByPlantInput) -> Decimal:
        itn = input_entity.itn
        sp = input_entity.sp
        sl = input_entity.sl
        ne = input_entity.Ne
        q = input_entity.q
        return Decimal((itn * sp * sl) / (ne * q))

    @classmethod
    def calculate_by_line_params(cls, input_entity: IrrigationTimeByLineInput) -> Decimal:
        itn = input_entity.itn
        se = input_entity.se
        sl = input_entity.sl
        q = input_entity.q
        return Decimal((itn * se * sl) / q)
