from decimal import Decimal
from pydantic import BaseModel


class ETcInput(BaseModel):
    P: Decimal
