from pydantic import BaseModel
from typing import List
from decimal import Decimal


class CropCoefficientResponse(BaseModel):
    crop_id: int
    crop_name: str
    crop_type: str
    kc_initial: Decimal
    kc_mid_season: Decimal
    kc_final: Decimal
    is_active: bool


class CropCoefficientListResponse(BaseModel):
    crop_coefficients: List[CropCoefficientResponse]


class CropCoefficientCreateResponse(BaseModel):
    created_id: int
    message: str = "Crop coefficient created successfully"


class CropCoefficientUpdateResponse(BaseModel):
    updated_id: int
    message: str = "Crop coefficient updated successfully"
