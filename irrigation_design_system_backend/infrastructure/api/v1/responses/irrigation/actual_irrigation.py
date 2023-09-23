from pydantic import BaseModel


class ActualIrrigationResponse(BaseModel):
    message: str = "actual irrigation calculated successfully."
    value: float
