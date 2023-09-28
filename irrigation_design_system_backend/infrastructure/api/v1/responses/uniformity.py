from pydantic import BaseModel


class UniformityResponse(BaseModel):
    message: str = "Uniformity in water distribution calculated successfully!"
    value: float
