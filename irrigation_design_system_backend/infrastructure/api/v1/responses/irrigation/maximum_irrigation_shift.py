from pydantic import BaseModel


class MaximumIrrigationShiftResponse(BaseModel):
    message: str = "maximum irrigation shift calculated successfully!"
    value: float
