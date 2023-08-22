from pydantic import BaseModel


class ITNResponse(BaseModel):
    message: str = "ITN calculation successful."
    value: float
