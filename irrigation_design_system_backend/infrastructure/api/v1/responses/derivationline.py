from pydantic import BaseModel


class DerivationLineDiameterResponse(BaseModel):
    message: str = "Successfully calculated derivation line diameter."
    value: float


class DerivationLineLoadLossResponse(BaseModel):
    message: str = "Successfully calculated bypass line load loss."
    value: float


class DerivationLineErrorResponse(BaseModel):
    message: str
