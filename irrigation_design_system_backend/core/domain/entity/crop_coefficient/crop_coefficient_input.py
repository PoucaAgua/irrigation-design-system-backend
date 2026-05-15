from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field


class CropCoefficientInput(BaseModel):
    crop_id: Optional[int] = Field(
        None, description="[ID] Identification of the crop in the database"
    )
    crop_name: Optional[str] = Field(None, description="[CROP_NAME] Name of the crop to be planted")
    crop_type: Optional[str] = Field(None, description="[CROP_TYPE] Type of the crop to be planted")
    kc_initial: Optional[Decimal] = Field(
        None, ge=0, description="[KC_INIT] Initial crop coefficient"
    )
    kc_mid_season: Optional[Decimal] = Field(
        None, ge=0, description="[KC_MID] Mid-season crop coefficient"
    )
    kc_final: Optional[Decimal] = Field(None, ge=0, description="[KC_END] Final crop coefficient")
    is_active: bool = Field(
        True, description="[ACTIVE] Crop coefficient status (True if active, False otherwise)"
    )
