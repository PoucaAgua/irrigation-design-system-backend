from decimal import Decimal
from dataclasses import dataclass
from core.domain.enum.hemisphere import Hemisphere
from core.domain.enum.month import MonthEnum


@dataclass
class EToHargreavesSamaniInput:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    latitude: Decimal
    month: MonthEnum


@dataclass
class EToBlanneyCriddleInputy:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    days: Decimal
    latitude: int
    month: MonthEnum
    hemisphere: Hemisphere


@dataclass
class EToPenmanMonteithInputyEntity:
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
