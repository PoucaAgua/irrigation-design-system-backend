from typing import List
from fastapi import APIRouter, HTTPException
from infrastructure.api.v1.responses.crop_coefficient import CropCoefficientCreateResponse
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from apps.crop_coefficient.crop_coefficient import CropCoefficientService

router = APIRouter()


@router.post("/crop_coefficients/upsert", response_model=CropCoefficientCreateResponse)
def create_crop_coefficient(crop_coefficient: CropCoefficientInput):
    created_coefficient = CropCoefficientService.upsert(crop_coefficient)
    return {"message": "Crop coefficient created successfully", "created_id": created_coefficient.id}


@router.get("/crop_coefficients/get_all/", response_model=List[CropCoefficientInput])
def get_all_crop_coefficients():
    return CropCoefficientService.get_all()


@router.get("/crop_coefficients/{crop_coefficient_id}/", response_model=CropCoefficientInput)
def get_crop_coefficient_by_id(crop_coefficient_id: int):
    crop_coefficient = CropCoefficientService.get_id(crop_coefficient_id)
    if crop_coefficient is None:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")
    return crop_coefficient
