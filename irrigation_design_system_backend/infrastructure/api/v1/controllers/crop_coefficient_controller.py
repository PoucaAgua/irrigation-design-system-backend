from fastapi import APIRouter
from apps.crop_coefficient.crop_coefficient_service import CropCoefficientService
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.api.v1.responses.crop_coefficient_response import CropCoefficientResponse

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
