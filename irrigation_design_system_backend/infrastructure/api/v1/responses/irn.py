from pydantic import BaseModel


class IRNResponse(BaseModel):
    message: str = "IRN calculation successful."
    value: float
