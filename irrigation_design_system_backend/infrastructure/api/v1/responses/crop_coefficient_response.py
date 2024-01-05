from pydantic import BaseModel
from typing import Optional


class CropCoefficientResponse(BaseModel):
    crop_id: Optional[int]
    crop_name: Optional[str]
    crop_type: Optional[str]
    kc_initial: Optional[float]
    kc_mid_season: Optional[float]
    kc_final: Optional[float]
    is_active: Optional[bool]
    status: Optional[str]
