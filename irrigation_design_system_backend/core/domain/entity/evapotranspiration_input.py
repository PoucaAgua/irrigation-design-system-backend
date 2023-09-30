from decimal import Decimal
from typing import Optional, Any

from pydantic import BaseModel, PositiveInt, model_validator

from core.domain.enum.hemisphere import Hemisphere
from core.domain.enum.month import MonthEnum


class EToHargravesSamaniInput(BaseModel):
    temperature_med: Decimal
    temperature_max: Decimal = None
    temperature_min: Decimal = None
    latitude: Decimal
    month: MonthEnum

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
