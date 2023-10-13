from pydantic import BaseModel


class CropCoefficientResponse(BaseModel):
    message: str = "Crop Coefficient successful!"
    crop_name: str
    crop_type: str
    kc_initial: float
    kc_mid_season: float
    kc_final: float
