from dataclasses import dataclass


@dataclass
class CropCoefficient:
    id: int
    crop_name: str
    crop_type: str
    kc_initial: float
    kc_mid_season: float
    kc_final: float

    @classmethod
    def create_from_json(cls, json: dict) -> "CropCoefficient":
        return cls(
            id=json.get("id"),
            crop_name=json["crop_name"],
            crop_type=json["crop_type"],
            kc_initial=float(json["kc_initial"]),
            kc_mid_season=float(json["kc_mid_season"]),
            kc_final=float(json["kc_final"]),
        )
