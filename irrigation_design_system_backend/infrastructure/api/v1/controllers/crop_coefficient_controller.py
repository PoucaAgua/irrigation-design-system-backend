from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends
from apps.crop_coefficient.crop_coefficient_service import CropCoefficientService
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.api.v1.responses.crop_coefficient_response import CropCoefficientResponse
from infrastructure.persistence.session import get_db

from infrastructure.persistence.repository.crop_coefficient_repository import \
    CropCoefficientRepository

router = APIRouter()

@router.post("/crop_coefficients", response_model=CropCoefficientResponse)
def create_or_update_crop_coefficient(crop_coefficient_entity: CropCoefficientInput):
    crop_coefficient = CropCoefficientService.upsert_crop_coefficient(crop_coefficient_entity)
    status_message = (
        "Crop coefficient created successfully"
        if not crop_coefficient.crop_id
        else "Crop coefficient updated successfully"
    )

    return CropCoefficientResponse(
        crop_id=crop_coefficient.crop_id,
        crop_name=crop_coefficient.crop_name,
        crop_type=crop_coefficient.crop_type,
        kc_initial=crop_coefficient.kc_initial,
        kc_mid_season=crop_coefficient.kc_mid_season,
        kc_final=crop_coefficient.kc_final,
        is_active=crop_coefficient.is_active,
        status=status_message,
    )

@router.get("/crop_coefficients/{crop_id}", response_model=CropCoefficientResponse)
def get_crop_coefficient_by_id(crop_id: int):
    db = get_db()
    crop_coefficient = CropCoefficientRepository().get_by_id(db, crop_id)
    if not crop_coefficient:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")

    return CropCoefficientResponse(
        crop_id=crop_coefficient.crop_id,
        crop_name=crop_coefficient.crop_name,
        crop_type=crop_coefficient.crop_type,
        kc_initial=crop_coefficient.kc_initial,
        kc_mid_season=crop_coefficient.kc_mid_season,
        kc_final=crop_coefficient.kc_final,
        is_active=crop_coefficient.is_active,
        status="Crop coefficient retrieved successfully"
    )


@router.get("/crop_coefficients", response_model=List[CropCoefficientResponse])
def get_all_crop_coefficients(db=Depends(get_db)):
    crop_coefficients = CropCoefficientService.get_all_crop_coefficients(db)
    if not crop_coefficients:
        raise HTTPException(status_code=404, detail="No crop coefficients found")

    return [
        CropCoefficientResponse(
            crop_id=crop.crop_id,
            crop_name=crop.crop_name,
            crop_type=crop.crop_type,
            kc_initial=crop.kc_initial,
            kc_mid_season=crop.kc_mid_season,
            kc_final=crop.kc_final,
            is_active=crop.is_active,
            status="Crop coefficient retrieved successfully"
        )
        for crop in crop_coefficients
    ]
