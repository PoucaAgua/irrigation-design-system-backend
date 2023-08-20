import pandas as pd
file_path = "C:\\Users\\Evellyn\\Desktop\\Nova pasta\\irrigation-design-system-backend\\irrigation_design_system_backend\\apps\\evapotranspiration\\data_radiation_hargraves_samani.csv"
import math
from _decimal import Decimal

def calculate_temperature_media(temperature_media=None, temperature_max=None, temperature_min=None, days=None):
    if temperature_media is not None:
        return temperature_media

    if temperature_max is not None and temperature_min is not None and days is not None and days != 0:  # Verifique se days é diferente de zero
        calculated_temperature_media = (temperature_max / days + temperature_min / days) / 2
        return calculated_temperature_media

    return None  

    


                             #### data_for_Hargreaves_Samani_radiation ####


import pandas as pd
def calculate_radiation_Hargreaves_Samani(latitude, month):
    file_path = "C:\\Users\\Evellyn\\Desktop\\Nova pasta\\irrigation-design-system-backend\\irrigation_design_system_backend\\apps\\evapotranspiration\\data_radiation_hargraves_samani.csv"
    data_radiation = pd.read_csv(file_path, sep=';', decimal=',', encoding='utf-8')

    print(data_radiation)
    
    filtered_df = data_radiation[data_radiation["latitude s"] == latitude]

    print(filtered_df)

    if not filtered_df.empty:
        rad_value = filtered_df[month.value].values[0]
        return Decimal(str(rad_value))
    else:
        return None
    


                ###### calculate_radiation_blanney_criddle ####

def calculate_radiation_blaney_criddle(latitude, month,hemisphere):
    file_path_norte = "C:\\Users\\Evellyn\\Desktop\\Nova pasta\\irrigation-design-system-backend\\irrigation_design_system_backend\\apps\\evapotranspiration\\data_north_sun_blanney_criddle.csv"
    file_path_sul = "C:\\Users\\Evellyn\\Desktop\\Nova pasta\\irrigation-design-system-backend\\irrigation_design_system_backend\\apps\\evapotranspiration\\data_south_sun_blanney_criddle.csv"
    
    valid_hemispheres = ['norte', 'sul']
    
    if hemisphere.lower() not in valid_hemispheres:
        return None  
    
    if hemisphere.lower() == 'norte':
        data = pd.read_csv(file_path_norte, delimiter=";")
        latitude_col = 'latitude norte'
    else:
        data = pd.read_csv(file_path_sul, delimiter=";")
        latitude_col = 'latitude sul'

    
    filtered_df = data[data[latitude_col] == latitude]
   
    if not filtered_df.empty:
        month_col = None
        for col in filtered_df.columns:
            if month.capitalize().strip() in col:
                month_col = col
                break
        
        if month_col is not None:
            rad_value = filtered_df[month_col].iloc[0]  
            return rad_value
        else:
            return None 
    else:
        return None


                             # # # penmanMonteithInputyEntity # # #



def calculate_vapor_saturation_pressure(temperature):
    # Equação de Buck
    es = 0.6108 * math.exp((17.27 * temperature) / (temperature + 237.3))
    return es

def calculate_vapor_current_pressure(relative_humidity_air, vapor_saturation_pressure):
        ea = (relative_humidity_air / 100) * vapor_saturation_pressure
        return ea

def calculate_declivity_curve_pressure_vapor(temperature, vapor_saturation_pressure):
        delta = (4098 * vapor_saturation_pressure) / ((temperature + 237.3) ** 2)
        return delta

def calculate_atmospheric_pressure(altitude):
        
        atmospheric_pressure = 101.3 * (293 - 0.0065 * altitude / 293.0) ** 5.23
        return atmospheric_pressure


def calculate_psychrometric_constant(atmospheric_pressure):
        gamma = 0.665 * 10**-3 * atmospheric_pressure
        return gamma



