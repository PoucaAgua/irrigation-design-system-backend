from pydantic import BaseModel


class IRNResponse(BaseModel):
    message: str = "actual irrigation calculated successfully."
    value: float
