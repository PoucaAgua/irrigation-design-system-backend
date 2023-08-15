import pandas as pd
file_path = "C:\\Users\\Evellyn\\Desktop\\Nova pasta\\irrigation-design-system-backend\\irrigation_design_system_backend\\apps\\evapotranspiration\\data_radiation_hargraves_samani.csv"
from io import StringIO
from _decimal import Decimal
# df = pd.read_csv(file_path, sep=';')

def calculate_temperature_media(temperature_media=None, temperature_max=None, temperature_min=None, days=None):
    if temperature_media is not None:
        return temperature_media
    
    if temperature_max is not None and temperature_min is not None and days is not None:
        calculated_temperature_media = (temperature_max / days + temperature_min / days) / 2
        return calculated_temperature_media
    
    return None


# temperature_media_calculate = calculate_temperature_media(temperature_max=6, temperature_min=3, days=3)
# print("Calculated media temperature:", temperature_media_calculate)


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
    


# #  input
# latitude = int(input("Digite a latitude: "))
# month_str = input("Digite o mês (Jan, Feb, ..., Dec): ")
# month = month_str.strip().capitalize() 

# rad_value = calculate_radiation__Hargreaves_Samani(latitude, month)
# if rad_value is not None:
#     print(f"Radiação em latitude {latitude}° e mês {month}: {rad_value}")
# else:
#     print("Dados não encontrados para a combinação de latitude e mês.")

    


                ###### calculate_radiation_blanney_criddle ####

def calculate_radiation_blanney_criddle(latitude, month,hemisphere):
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

# # input
# latitude = int(input("Digite a latitude: "))
# month = input("Digite o mês (Jan, Feb, ..., Dec): ")
# hemisphere = input("Digite o hemisfério (norte ou sul): ")

# rad_value = calculate_radiation_blanney_criddle(latitude, month, hemisphere)
# if rad_value is not None:
#     print(f"Radiação em {hemisphere} em {month} para {latitude}°: {rad_value}")
# else:
#     print(f"Dados não encontrados para a combinação de latitude, mês e hemisfério.")