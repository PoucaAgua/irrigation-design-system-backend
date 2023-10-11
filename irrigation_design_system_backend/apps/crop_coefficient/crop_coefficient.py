from dataclasses import dataclass

@dataclass
class CropCoefficientData:
    crop_name: str  # Crop name
    crop_type: str  # Crop type
    kc_initial: float  # KC for the initial phase
    kc_mid_season: float  # KC for the mid-season
    kc_final: float  # KC for the final phase
