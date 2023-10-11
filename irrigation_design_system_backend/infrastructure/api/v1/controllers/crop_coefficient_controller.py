from fastapi import APIRouter
from infrastructure.api.v1.responses.crop_coefficient import CropCoefficientResponse
from apps.crop_coefficient.crop_coefficient import CropCoefficientData

router = APIRouter()


@router.post("", response_model=CropCoefficientResponse)
def crop_coefficient(cropcoefficient: CropCoefficientData):
    results = CropCoefficientResponse(
        crop_name=cropcoefficient.crop_name,
        crop_type=cropcoefficient.crop_type,
        kc_initial=cropcoefficient.kc_initial,
        kc_mid_season=cropcoefficient.kc_mid_season,
        kc_final=cropcoefficient.kc_final)
    return results

