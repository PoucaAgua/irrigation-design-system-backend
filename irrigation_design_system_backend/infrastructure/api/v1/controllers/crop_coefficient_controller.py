from typing import List
from fastapi import APIRouter, HTTPException
from apps.crop_coefficient.crop_coefficient import (
    CropCoefficientService,
)
from core.domain.entity.crop_coefficient_input import (
    CropCoefficientInput,
)
from infrastructure.api.v1.responses.crop_coefficient import (
    CropCoefficientCreateResponse,
    CropCoefficientListResponse,
    CropCoefficientResponse,
    CropCoefficientUpdateResponse,
)

router = APIRouter()


@router.post("/crop_coefficients/upsert", response_model=CropCoefficientCreateResponse)
def create_crop_coefficient(crop_coefficient: CropCoefficientInput):
    created_coefficient = CropCoefficientService.upsert(crop_coefficient)
    return {
        "message": "Crop coefficient created successfully",
        "created_id": created_coefficient.id,
    }


@router.get("/crop_coefficients/get_all/", response_model=List[CropCoefficientListResponse])
def get_all_crop_coefficients():
    return CropCoefficientService.get_all()


@router.get("/crop_coefficients/{crop_coefficient_id}/", response_model=CropCoefficientResponse)
def get_crop_coefficient_by_id(crop_coefficient_id: int):
    crop_coefficient = CropCoefficientService.get_id(crop_coefficient_id)
    if crop_coefficient is None:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")
    return crop_coefficient


@router.delete("/crop_coefficients/{crop_coefficient_id}/", response_model=dict)
def delete_crop_coefficient(crop_coefficient_id: int):
    deleted = CropCoefficientService.delete(crop_coefficient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")
    return {"message": "Crop coefficient deleted successfully"}


@router.put(
    "/crop_coefficients/{crop_coefficient_id}/", response_model=CropCoefficientUpdateResponse
)
def update_crop_coefficient(crop_coefficient_id: int, updated_coefficient: CropCoefficientInput):
    existing_coefficient = CropCoefficientService.get_id(crop_coefficient_id)
    if existing_coefficient is None:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")

    updated_coefficient.id = crop_coefficient_id

    updated = CropCoefficientService.update(crop_coefficient_id, updated_coefficient)
    if not updated:
        raise HTTPException(status_code=400, detail="Failed to update crop coefficient")

    return {
        "updated_id": crop_coefficient_id,
        "message": "Crop coefficient updated successfully",
    }
