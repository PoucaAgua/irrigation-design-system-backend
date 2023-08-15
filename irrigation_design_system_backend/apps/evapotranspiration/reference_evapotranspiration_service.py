from _decimal import Decimal



from core.constants.evapotranspiration import ReferenceEvapotranspirationConstants
from core.domain.entity.evapotranspiration_entity import EToEntity, EToHargravesSamaniInputyEntity
import pandas as pd
from .funcitions_to_reference_evapotranspiration import (calculate_temperature_media, calculate_radiation_Hargreaves_Samani, calculate_radiation_blanney_criddle )



parameters_hargraves_samani = ReferenceEvapotranspirationConstants.parameters_hargraves_samani
parameters_blaney_cridlle = ReferenceEvapotranspirationConstants.parameters_blaney_cridlle
parameters_penman_monteith = ReferenceEvapotranspirationConstants.parameters_penman_monteith


class ReferenceEvapotranspirationService:
    @staticmethod
    def calculate_hargraves_samani(eto_entity: EToHargravesSamaniInputyEntity) -> Decimal:
        a, b, c = parameters_hargraves_samani
        Ra =  calculate_radiation_Hargreaves_Samani(latitude=eto_entity.latitude, month=eto_entity.month)
        Tmed = eto_entity.temperature_med
        Tmin = eto_entity.temperature_min
        Tmax = eto_entity.temperature_max
        return Decimal(Ra * a * (b * (Tmed + c) * (Tmax - Tmin)) ** Decimal(0.5))
    


    @staticmethod
    def calculate_blaney_cridlle(eto_entity: EToEntity) -> Decimal:
        a, b, c = parameters_blaney_cridlle
        P = calculate_radiation_blanney_criddle( latitude=eto_entity.latitude, month=eto_entity.month)
        Tmed = calculate_temperature_media(temperature_max=eto_entity.temperature_max, temperature_min=eto_entity.temperature_min, days=eto_entity.days, hemisphere =eto_entity.hemispherse)
        return Decimal((a * Tmed + b)* P / c )
    # ajeitar o Ra - adicionar uma função (pandas)


    @staticmethod
    def calculate_penman_monteith(eto_entity: EToEntity) -> Decimal:
        a, b, c, d, e = parameters_penman_monteith
        slop = eto_entity.slop
        Ra = eto_entity.radiation_net
        g = eto_entity.ground_heat
        y = eto_entity.psychrometric_constant
        Tair = eto_entity.temperature_air
        u2 = eto_entity.wind_speed
        es = eto_entity.vapor_saturation_pressure
        ea = eto_entity.vapor_current_pressure
        return Decimal(a * slop * (Ra - g) + y * b/(Tair+c) )









    

