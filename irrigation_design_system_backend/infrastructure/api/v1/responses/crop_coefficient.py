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
    message: str


class CropCoefficientUpdateResponse(BaseModel):
    message: str


class CropCoefficientDeleteResponse(BaseModel):
    message: str
