from pydantic import BaseModel


class TotalIrrigationResponse(BaseModel):
    message: str = "total irrigation calculated successfully!"
    value: float
