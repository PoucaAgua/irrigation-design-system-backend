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
    slop: Decimal #Declividade da curva de pressão de vapor de saturação = s (delta)
    radiation_net: Decimal   #radiação líquida na superfície da Terra = Rn
    ground_heat: Decimal #fluxo de calor do solo = G
    psychrometric_constant: Decimal #constante psicrométrica = Y
    temperature_air: Decimal # = Tair
    wind_speed: Decimal #Velocidade do vento a 2 m de altura = U2
    vapor_saturation_pressure: Decimal #Pressão da saturação do vapor = es 
    vapor_current_pressure: Decimal #pressão atual do vapor = ea
    days: Decimal
    latitude: Decimal
    month: Decimal
    hemispherse: Hemispherse

@dataclass
class EToHargravesSamaniInputyEntity:
    temperature_med: Decimal
    temperature_max: Decimal
    temperature_min: Decimal
    latitude: int
    month: Month
