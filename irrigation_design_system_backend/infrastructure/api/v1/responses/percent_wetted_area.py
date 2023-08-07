from pydantic import BaseModel

class IBTResponse(BaseModel):
    message: str = "Tree irrigation calculation successful."
    value: float

class TSWResponse(BaseModel):
    message: str = "Saturated wetted radius calculation successful."
    value: float

class CPResponse(BaseModel):
    message: str = "Maximum percentage of area wetted by the dripper calculation successful."
    value: float