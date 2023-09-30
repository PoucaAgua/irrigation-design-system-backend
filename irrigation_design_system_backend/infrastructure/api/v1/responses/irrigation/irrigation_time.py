from pydantic import BaseModel


class IrrigationTimeResponse(BaseModel):
    message: str = "Irrigation time (hour) calculated successfully."
    value: float
