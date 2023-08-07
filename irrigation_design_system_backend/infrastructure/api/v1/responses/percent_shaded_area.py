from pydantic import BaseModel


class PercentShadedAreaByStripResponse(BaseModel):
    message: str = "Ps by the plant' strip calculation successful."
    value: float


class PercentShadedAreaByCanopyResponse(BaseModel):
    message: str = "Ps by plant's canopy projection calculation successful."
    value: float
