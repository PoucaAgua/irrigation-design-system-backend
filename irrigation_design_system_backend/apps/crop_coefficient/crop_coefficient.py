from pydantic import BaseModel
from decimal import Decimal

class CropCoefficientData(BaseModel):
    id: int
    crop_name: str
    crop_type: str
    kc_initial: Decimal
    kc_mid_season: Decimal
    kc_final: Decimal
