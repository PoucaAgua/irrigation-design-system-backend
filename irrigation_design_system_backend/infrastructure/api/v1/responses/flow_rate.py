from pydantic import BaseModel

class FlowRateResponse(BaseModel):
    message: str = "Emitter flow calculated successfully!"
    value: float