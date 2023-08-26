from pydantic import BaseModel

class LateralLineResponse(BaseModel):
    message: str = "Lateral Line calculation successful."
    value: float
