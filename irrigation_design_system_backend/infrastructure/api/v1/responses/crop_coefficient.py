from pydantic import BaseModel
from typing import List


class CropCoefficientResponse(BaseModel):
    id: int
    crop_name: str
    crop_type: str
    kc_initial: float
    kc_mid_season: float
    kc_final: float
    active: bool


class CropCoefficientListResponse(BaseModel):
    crop_coefficients: List[CropCoefficientResponse]


class CropCoefficientCreateResponse(BaseModel):
    created_id: int
    message: str = "Crop coefficient created successfully"


class CropCoefficientUpdateResponse(BaseModel):
    updated_id: int
    updated_fields: List[str]
    message: str = "Crop coefficient updated successfully"


class CropCoefficientDeleteResponse(BaseModel):
    deleted_id: int
    message: str = "Crop coefficient deleted successfully"
