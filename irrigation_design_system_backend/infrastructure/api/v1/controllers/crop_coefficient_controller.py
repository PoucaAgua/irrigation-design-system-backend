from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends
from infrastructure.api.v1.responses.crop_coefficient import CropCoefficientCreateResponse
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from apps.crop_coefficient.crop_coefficient import CropCoefficientService
from infrastructure.persistence.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/crop_coefficients/upsert", response_model=CropCoefficientCreateResponse)
def create_crop_coefficient(crop_coefficient: CropCoefficientInput, db: Session = Depends(get_db)):
    CropCoefficientService.upsert(crop_coefficient, db)
    return {"message": "Crop coefficient created successfully"}


@router.get("/crop_coefficients/get_all", response_model=List[CropCoefficientInput])
def get_all_crop_coefficients(db: Session = Depends(get_db)):
    crop_coefficients = CropCoefficientService.get_all(db)
    return crop_coefficients


@router.get("/crop_coefficients/{crop_coefficient_id}", response_model=CropCoefficientInput)
def get_crop_coefficient_by_id(crop_coefficient_id: int, db: Session = Depends(get_db)):
    crop_coefficient = CropCoefficientService.get_id(db, crop_coefficient_id)
    if crop_coefficient is None:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")
    return crop_coefficient
