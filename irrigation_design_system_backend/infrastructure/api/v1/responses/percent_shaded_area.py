from pydantic import BaseModel

class SAResponse(BaseModel):
    message: str = "Shaded strip by the plant calculation successful."
    value: float

class CPResponse(BaseModel):
    message: str = "Diameter of the plant's canopy projection calculation successful."
    value: float