from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.api.v1.responses.crop_coefficient import (
    CropCoefficientResponse,
    CropCoefficientListResponse,
    CropCoefficientCreateResponse,
    CropCoefficientUpdateResponse,
    CropCoefficientDeleteResponse,
)
from core.domain.entity.crop_coefficient_entity import CropCoefficientEntity
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)
from infrastructure.persistence.session import get_db

router = APIRouter()


@router.post("/crop_coefficients/", response_model=CropCoefficientCreateResponse)
def create_crop_coefficient(crop_coefficient: CropCoefficientEntity, db: Session = Depends(get_db)):
    crop_coefficient_repository = CropCoefficientRepository(db)
    crop_coefficient_repository.create_crop_coefficient(
        crop_coefficient.crop_name,
        crop_coefficient.crop_type,
        crop_coefficient.kc_initial,
        crop_coefficient.kc_mid_season,
        crop_coefficient.kc_final,
    )
    return {"message": "Crop coefficient created successfully"}


@router.get("/crop_coefficients/{crop_coefficient_id}/", response_model=CropCoefficientResponse)
def read_crop_coefficient(crop_coefficient_id: int, db: Session = Depends(get_db)):
    crop_coefficient_repository = CropCoefficientRepository(db)
    db_crop_coefficient = crop_coefficient_repository.get_crop_coefficient(crop_coefficient_id)
    if db_crop_coefficient is None:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")
    return db_crop_coefficient


@router.get("/crop_coefficients/", response_model=CropCoefficientListResponse)
def read_crop_coefficients(db: Session = Depends(get_db)):
    crop_coefficient_repository = CropCoefficientRepository(db)
    crop_coefficients = crop_coefficient_repository.get_all_crop_coefficients()
    return {"crop_coefficients": crop_coefficients}


@router.put(
    "/crop_coefficients/{crop_coefficient_id}/", response_model=CropCoefficientUpdateResponse
)
def update_crop_coefficient(
    crop_coefficient_id: int, crop_coefficient: CropCoefficientEntity, db: Session = Depends(get_db)
):
    crop_coefficient_repository = CropCoefficientRepository(db)
    db_crop_coefficient = crop_coefficient_repository.get_crop_coefficient(crop_coefficient_id)
    if db_crop_coefficient is None:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")

    if crop_coefficient.active in [0, 1]:
        db_crop_coefficient.active = crop_coefficient.active

    crop_coefficient_repository.update_crop_coefficient(
        crop_coefficient_id,
        crop_coefficient.crop_name,
        crop_coefficient.crop_type,
        crop_coefficient.kc_initial,
        crop_coefficient.kc_mid_season,
        crop_coefficient.kc_final,
    )

    return {"message": "Crop coefficient updated successfully"}


@router.delete(
    "/crop_coefficients/{crop_coefficient_id}/", response_model=CropCoefficientDeleteResponse
)
def delete_crop_coefficient(crop_coefficient_id: int, db: Session = Depends(get_db)):
    crop_coefficient_repository = CropCoefficientRepository(db)
    success = crop_coefficient_repository.delete_crop_coefficient(crop_coefficient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Crop coefficient not found")
    return {"message": "Crop coefficient deleted successfully"}
