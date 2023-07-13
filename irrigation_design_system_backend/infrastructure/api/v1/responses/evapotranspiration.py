from pydantic import BaseModel


class EvapotranspirationResponse(BaseModel):
    message: str = "Evapotranspiration calculation successful."
    value: float
