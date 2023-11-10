from decimal import Decimal
from pydantic import BaseModel


class CropEvapotranspirationInput(BaseModel):
    Eto: Decimal
    Kc: Decimal
    Kl: Decimal
    P: Decimal
