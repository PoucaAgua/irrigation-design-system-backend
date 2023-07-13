from decimal import Decimal
from dataclasses import dataclass


@dataclass
class EToData:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    radiation: Decimal

    @classmethod
    def create_from_json(cls, json: dict) -> "EToData":
        return cls(
            temperature_med=Decimal(json["temperature_med"]),
            temperature_max=Decimal(json["temperature_max"]),
            temperature_min=Decimal(json["temperature_min"]),
            radiation=Decimal(json["radiation"])
        )
