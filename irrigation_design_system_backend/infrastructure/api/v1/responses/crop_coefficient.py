from pydantic import BaseModel


class CropCoefficientResponse(BaseModel):
    message: str = "Crop Coefficient successful!"
    crop_name: str  # Crop name (text)
    crop_type: str  # Crop type (text)
    kc_initial: float  # KC for the initial phase (float)
    kc_mid_season: float  # KC for the mid-season (float)
    kc_final: float  # KC for the final phase (float)
