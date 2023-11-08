from fastapi import APIRouter

from apps.crop_coefficient.crop_coefficient import CropCoefficientService
from infrastructure.api.v1.responses.crop_coefficient import (
    CropCoefficientCreateResponse,
)
from core.domain.entity.crop_coefficient_input import CropCoefficientInput


router = APIRouter()


@router.post("/crop_coefficients/", response_model=CropCoefficientCreateResponse)
def create_crop_coefficient(crop_coefficient: CropCoefficientInput):
    CropCoefficientService.upsert(crop_coefficient)
    return {"message": "Crop coefficient created successfully"}

