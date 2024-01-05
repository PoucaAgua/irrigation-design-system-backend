from pydantic import BaseModel


class CropCoefficientInput(BaseModel):
    crop_id: int
    crop_name: str
    crop_type: str
    kc_initial: float
    kc_mid_season: float
    kc_final: float
    is_active: bool
