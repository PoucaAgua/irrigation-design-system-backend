from pydantic import BaseModel


class IrrigationTreeResponse(BaseModel):
    message: str = "Pw by Tree irrigation calculation successful."
    value: float


class SaturatedWetRadiusX2Response(BaseModel):
    message: str = "Pw by Twice the saturated wetted radius calculation successful."
    value: float


class ContinuousStripResponse(BaseModel):
    message: str = (
        "Pw by Maximum percentage of area wetted by the dripper calculation successful."
    )
    value: float
