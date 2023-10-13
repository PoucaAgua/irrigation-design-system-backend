from dataclasses import dataclass


@dataclass
class CropCoefficientData:
    crop_name: str
    crop_type: str
    kc_initial: float
    kc_mid_season: float
    kc_final: float
