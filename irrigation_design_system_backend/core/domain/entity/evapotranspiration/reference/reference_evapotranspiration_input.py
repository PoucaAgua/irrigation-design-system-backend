from decimal import Decimal
from typing import Any
from pydantic import BaseModel, PositiveInt, model_validator
from core.domain.enum.hemisphere import Hemisphere
from core.domain.enum.month import MonthEnum
from core.domain.entity.evapotranspiration.temperature_med import calculate_temperature_med


class EToHargravesSamaniInput(BaseModel):
    temperature_med: Decimal
    temperature_max: Decimal = None
    temperature_min: Decimal = None
    latitude: Decimal
    month: MonthEnum

    @model_validator(mode="before")
    @classmethod
    def check(cls, data: Any) -> Any:
        data["temperature_med"] = calculate_temperature_med(**data)
        return data


class EToBlanneyCriddleInput(BaseModel):
    temperature_med: Decimal
    temperature_max: Decimal = None
    temperature_min: Decimal = None
    latitude: PositiveInt
    hemisphere: Hemisphere
    month: MonthEnum

    @model_validator(mode="before")
    @classmethod
    def check(cls, data: Any) -> Any:
        data["temperature_med"] = calculate_temperature_med(**data)
        return data


class EToPenmanMonteithInput(BaseModel):
    temperature_med: float
    temperature_max: float = None
    temperature_min: float = None
    relative_humidity_air: float
    days: float
    altitude: float
    wind_speed: float
    ground_heat: float
    daily_radiation: float

    @model_validator(mode="before")
    @classmethod
    def check(cls, data: Any) -> Any:
        data["temperature_med"] = calculate_temperature_med(**data)
        return data
