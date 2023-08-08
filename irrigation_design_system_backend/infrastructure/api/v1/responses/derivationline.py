from pydantic import BaseModel


class DerivationlineReponse(BaseModel):
    message: str = "Derivation line calculation successful."
    value: float