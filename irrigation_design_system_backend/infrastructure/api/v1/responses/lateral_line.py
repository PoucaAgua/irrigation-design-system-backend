from pydantic import BaseModel
from _decimal import Decimal


class LateralLineDiameterResponse(BaseModel):
    message: str = "Successfully calculated lateral line diameter."
    value: float


class LateralLineHeadLossResponse(BaseModel):
    message: str = "Successfully calculated bypass line load loss."
    value: float


class LateralLineErrorResponse(BaseModel):
    message: str
