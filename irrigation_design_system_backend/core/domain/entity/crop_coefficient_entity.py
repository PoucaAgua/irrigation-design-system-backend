from dataclasses import dataclass


@dataclass
class CropCoefficient:
    crop_name: str  # Crop name (text)
    crop_type: str  # Crop type (text)
    kc_initial: float  # KC for the initial phase (float)
    kc_mid_season: float  # KC for the mid-season (float)
    kc_final: float  # KC for the final phase (float)

    @classmethod
    def create_from_json(cls, json: dict) -> "CropCoefficient":
        return cls(
            crop_name=json["crop_name"],
            crop_type=json["crop_type"],
            kc_initial=float(json["kc_initial"]),
            kc_mid_season=float(json["kc_mid_season"]),
            kc_final=float(json["kc_final"]),
        )
