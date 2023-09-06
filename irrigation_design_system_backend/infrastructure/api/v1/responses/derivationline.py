from pydantic import BaseModel


class DerivationlineDiameterReponse(BaseModel):
    message: str = "Successfully calculated derivation line diameter."
    value: float

class DerivationlineLoadLossReponse(BaseModel):
    message: str = "Successfully calculated bypass line load loss."
    value: float