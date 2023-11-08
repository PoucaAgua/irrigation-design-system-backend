from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class CropCoefficientInput(BaseModel):
    id: Optional[int] = None
    crop_name: Optional[str] = None
    crop_type: Optional[str] = None
    kc_initial: Optional[Decimal] = None
    kc_mid_season: Optional[Decimal] = None
    kc_final: Optional[Decimal] = None
    active: bool = True
