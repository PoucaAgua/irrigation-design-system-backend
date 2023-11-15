from pydantic import BaseModel


class SpecialPartsReponse(BaseModel):
    message: str = "Successfully calculated special parts load loss."
    value: float
