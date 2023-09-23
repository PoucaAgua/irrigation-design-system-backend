from core.domain.entity.irrigation.maximum_irrigation_shift_input import MaximumIrrigationShiftInput


class MaximumIrrigationShiftService:
    @classmethod
    def calculate(cls, maximum_irrigation_shift_input: MaximumIrrigationShiftInput) -> int:
        irn = maximum_irrigation_shift_input.actual_irrigation
        etc = maximum_irrigation_shift_input.crop_evapotranspiration
        return int(irn / etc)
