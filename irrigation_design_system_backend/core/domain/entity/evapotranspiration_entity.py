from decimal import Decimal
from dataclasses import dataclass
from core.domain.enum.hemispherse import Hemispherse    
from core.domain.enum.month import Month


@dataclass
class EToEntity:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    radiation: Decimal
    humidity: Decimal
    psychrometric_constant: Decimal 
    days: Decimal
    latitude: Decimal
    month: Decimal
    hemispherse: Hemispherse
    relative_humidity_air: float #umidade relativa do ar RH 
    temperature_med: float
    temperature_max: float
    temperature_min: float
    days: float
    altitude: float
    wind_speed: float
    ground_heat: float 
    daily_radiation: float
    latitude: int

@dataclass
class EToHargravesSamaniInputyEntity:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    latitude: int
    month: Month

@dataclass
class EToBlanneyCriddleInputyEntity:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    latitude: int
    month: Month
    days: Decimal
    hemispherse: Hemispherse


@dataclass
class EToPenmanMonteithInputyEntity:
    temperature_med: float
    relative_humidity_air: float #umidade relativa do ar RH 
    temperature_med: float
    temperature_max: float
    temperature_min: float
    days: float
    altitude: float
    wind_speed: float #Velocidade do vento a 2 m de altura = U2
    ground_heat: float #fluxo de calor do solo = G
    daily_radiation: float  #radiação líquida na superfície da Terra = Rn
    
    


