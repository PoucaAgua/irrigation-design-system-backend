from pydantic import BaseModel, validator
from _decimal import Decimal


class OutputFloat(BaseModel):
    value: Decimal

    @validator("value", pre=True, always=True)
    def round_value(cls, v):
        return f"{v:.2f}"
