from decimal import Decimal
from dataclasses import dataclass
from typing import Optional, Any

from pydantic import BaseModel, PositiveInt, model_validator

from core.domain.enum.hemisphere import Hemisphere
from core.domain.enum.month import MonthEnum


@dataclass
class EToHargravesSamaniInput:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    latitude: Decimal
    month: MonthEnum


class EToBlanneyCriddleInput(BaseModel):
    temperature_med: Decimal
    temperature_max: Decimal = None
    temperature_min: Decimal = None
    latitude: PositiveInt
    month: MonthEnum
    hemisphere: Hemisphere

    @model_validator(mode="before")
    @classmethod
    def check(cls, data: Any) -> Any:
        data["temperature_med"] = cls.__temperature_med(**data)
        return data

    @staticmethod
    def __temperature_med(
            temperature_med: Optional[Decimal] = None,
            temperature_max: Optional[Decimal] = None,
            temperature_min: Optional[Decimal] = None,
            **kwargs
    ):
        if temperature_med is not None:
            return temperature_med

        if temperature_max is not None and temperature_min is not None:
            return (temperature_max + temperature_min) / 2

        raise ValueError(
            "Needs to have temperature_med or both temperature_max and temperature_min"
        )


@dataclass
class EToPenmanMonteithInput:
    temperature_med: float
    relative_humidity_air: float  # umidade relativa do ar RH
    temperature_med: float
    temperature_max: float
    temperature_min: float
    days: float
    altitude: float
    wind_speed: float  # Velocidade do vento a 2 m de altura = U2
    ground_heat: float  # fluxo de calor do solo = G
    daily_radiation: float  # radiação líquida na superfície da Terra = Rn .
