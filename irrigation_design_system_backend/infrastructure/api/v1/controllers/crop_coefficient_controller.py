from typing import List
from fastapi import APIRouter, HTTPException
from apps.crop_coefficient.crop_coefficient_service import CropCoefficientService
from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput
from infrastructure.api.v1.responses.crop_coefficient_responses import CropCoefficientResponse

router = APIRouter()


@router.post("/crop_coefficients/upsert", response_model=CropCoefficientResponse)
def upsert_crop_coefficient(crop_coefficient: CropCoefficientInput):
    return CropCoefficientService.upsert(crop_coefficient)
