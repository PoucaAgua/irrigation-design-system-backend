from typing import List
from fastapi import APIRouter, HTTPException
from infrastructure.api.v1.responses.crop_coefficient import CropCoefficientResponse
from apps.crop_coefficient.crop_coefficient import CropCoefficientData
from infrastructure.persistence.repository.crop_coefficient_repository import (
    crop_coefficient_post,
    crop_coefficient_get_id,
    crop_coefficients_get_all,
    crop_coefficient_active,
    crop_coefficient_update,
    crop_coefficient_delete,
)

router = APIRouter()


@router.post("/post", response_model=CropCoefficientResponse)
def crop_coefficient_post_router(cropcoefficient: CropCoefficientData):
    db_cropcoefficient = crop_coefficient_post(cropcoefficient)
    return db_cropcoefficient


@router.get("/get_id/{get_id}", response_model=CropCoefficientResponse)
def crop_coefficient_get_id_router(get_id: int):
    db_cropcoefficient = crop_coefficient_get_id(get_id)
    if db_cropcoefficient:
        return CropCoefficientResponse(
            message="Crop Coefficient get id successfully",
            id=db_cropcoefficient.id,
            crop_name=db_cropcoefficient.crop_name,
            crop_type=db_cropcoefficient.crop_type,
            kc_initial=db_cropcoefficient.kc_initial,
            kc_mid_season=db_cropcoefficient.kc_mid_season,
            kc_final=db_cropcoefficient.kc_final,
        )
    raise HTTPException(status_code=404, detail="Recurso não encontrado")


@router.get("/get_all", response_model=List[CropCoefficientResponse])
def crop_coefficients_get_all_router():
    db_crop_coefficients = crop_coefficients_get_all()
    response = [
        CropCoefficientResponse(
            message="Crop Coefficient get all successfully",
            id=db_crop_coefficient.id,
            crop_name=db_crop_coefficient.crop_name,
            crop_type=db_crop_coefficient.crop_type,
            kc_initial=db_crop_coefficient.kc_initial,
            kc_mid_season=db_crop_coefficient.kc_mid_season,
            kc_final=db_crop_coefficient.kc_final,
        )
        for db_crop_coefficient in db_crop_coefficients
    ]
    return response


@router.post("/active/{get_id}", response_model=CropCoefficientResponse)
def crop_coefficient_active_router(get_id: int, active: bool):
    db_cropcoefficient = crop_coefficient_active(get_id, active)

    if db_cropcoefficient:
        response = CropCoefficientResponse(
            message="Crop Coefficient activate successfully",
            id=db_cropcoefficient.id,
            crop_name=db_cropcoefficient.crop_name,
            crop_type=db_cropcoefficient.crop_type,
            kc_initial=db_cropcoefficient.kc_initial,
            kc_mid_season=db_cropcoefficient.kc_mid_season,
            kc_final=db_cropcoefficient.kc_final,
        )
        return response
    else:
        raise HTTPException(status_code=404, detail="Recurso não encontrado")


@router.put("/update/{get_id}", response_model=CropCoefficientResponse)
def crop_coefficient_update_router(get_id: int, update_data: CropCoefficientData):
    db_cropcoefficient = crop_coefficient_update(get_id, update_data)

    if db_cropcoefficient:
        response = CropCoefficientResponse(
            message="Crop Coefficient updated successfully",
            id=db_cropcoefficient.id,
            crop_name=db_cropcoefficient.crop_name,
            crop_type=db_cropcoefficient.crop_type,
            kc_initial=db_cropcoefficient.kc_initial,
            kc_mid_season=db_cropcoefficient.kc_mid_season,
            kc_final=db_cropcoefficient.kc_final,
        )
        return response
    else:
        raise HTTPException(status_code=404, detail="Recurso não encontrado")


@router.delete("/delete/{get_id}", response_model=CropCoefficientResponse)
def crop_coefficient_delete_router(get_id: int):
    crop_coefficient_delete(get_id)

    response = CropCoefficientResponse(
        message="Crop Coefficient deleted successfully",
        id=get_id,
        crop_name="",
        crop_type="",
        kc_initial=0.0,
        kc_mid_season=0.0,
        kc_final=0.0,
    )
    return response
