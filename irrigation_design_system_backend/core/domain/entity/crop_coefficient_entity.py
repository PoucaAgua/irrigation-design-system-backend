from decimal import Decimal
from pydantic import BaseModel


class CropCoefficientEntity(BaseModel):
    id: int
    crop_name: str
    crop_type: str
    kc_initial: Decimal
    kc_mid_season: Decimal
    kc_final: Decimal
    active: int
