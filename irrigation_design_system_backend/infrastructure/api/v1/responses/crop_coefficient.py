from pydantic import BaseModel


class CropCoefficientResponse(BaseModel):
    id: int
    message: str = "Crop Coefficient post successful!"
    crop_name: str
    crop_type: str
    kc_initial: float
    kc_mid_season: float
    kc_final: float
