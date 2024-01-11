from typing import List
from fastapi import APIRouter, HTTPException
from apps.crop_coefficient.crop_coefficient_service import CropCoefficientService
from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput
from infrastructure.api.v1.responses.crop_coefficient_responses import CropCoefficientResponse

router = APIRouter()


@router.post("/crop_coefficients/upsert", response_model=CropCoefficientResponse)
def upsert_crop_coefficient(crop_coefficient: CropCoefficientInput):
    return CropCoefficientService.upsert(crop_coefficient)


@router.get("/crop_coefficients/get_all/", response_model=List[CropCoefficientResponse])
def get_all_crop_coefficients():
    return CropCoefficientService.get_all()


@router.get("/crop_coefficients/{crop_coefficient_id}/", response_model=CropCoefficientInput)
def get_crop_coefficient_by_id(crop_coefficient_id: int):
    crop_coefficient = CropCoefficientService.get_id(crop_coefficient_id)
    if crop_coefficient is None:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")
    return crop_coefficient
