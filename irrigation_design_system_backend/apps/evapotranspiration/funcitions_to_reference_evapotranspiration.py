import math
from _decimal import Decimal
from core.tables.evapotraspiration_tables import EvapotranspirationDfTable
from core.domain.enum.hemisphere import Hemisphere

# def calculate_radiation_Hargreaves_Samani(latitude, month):

#     df_radiation = EvapotranspirationDfTable.DF_RADIATION_HARGRAVES_SAMANI()

#     filtered_df = df_radiation[df_radiation["latitude s"] == latitude]
#     interpolated_df = df_radiation.iloc[::2].copy()

#     if not interpolated_df.empty:
#         rad_value = interpolated_df[month.value].values[0]  # Use diretamente o nome do mês
#         return Decimal(str(rad_value))


def calculate_radiation_Hargreaves_Samani(latitude, month):

    df_radiation = EvapotranspirationDfTable.DF_RADIATION_HARGRAVES_SAMANI()
    filtered_df = df_radiation[df_radiation["latitude s"] == latitude]

    if not filtered_df .empty:
        rad_value = filtered_df [month.value].values[0]
        return Decimal(str(rad_value))
    
    
def calculate_temperature_media(temperature_media: Decimal, temperature_max: Decimal, temperature_min: Decimal, days: Decimal):
    if temperature_media is not None:
        return temperature_media

    if temperature_max is not None and temperature_min is not None and days is not None and days != 0:
        calculated_temperature_media = (temperature_max / days + temperature_min / days) / 2
        return calculated_temperature_media


def calculate_radiation_blaney_criddle(latitude, hemisphere, month):
    df_data_dict = {
        Hemisphere.NORTE: EvapotranspirationDfTable.DF_DATA_NORTH_SUN_BLANNEY_CRIDDLE(),
        Hemisphere.SUL: EvapotranspirationDfTable.DF_DATA_SOUTH_SUN_BLANNEY_CRIDDLE()
    }

    if hemisphere == "NORTE":
        hemisphere_enum = Hemisphere.NORTE
    elif hemisphere == "SUL":
        hemisphere_enum = Hemisphere.SUL
    else:
        raise ValueError("Invalid hemisphere value")

    data = df_data_dict[hemisphere_enum]
    filtered_df = data[data['latitude'] == latitude]

    if not filtered_df.empty:
        if month in filtered_df.columns:
            rad_value = filtered_df[month.value].iloc[0]
            print(rad_value)
    # print(f"hemisphere_enum: {hemisphere_enum}")
    # print(f"latitude: {latitude}")
    # print(f"month.value: {month.value}")
    # print(f"filtered_df: {filtered_df}")
    # print(f"filtered_df.columns: {filtered_df.columns}")
    # print(f"rad_value: {rad_value}")
            # return Decimal(str(rad_value))

  
# def calculate_radiation_blaney_criddle(latitude, hemisphere, month):
#     df_data_dict = {
#         Hemisphere.NORTE: EvapotranspirationDfTable.DF_DATA_NORTH_SUN_BLANNEY_CRIDDLE(),
#         Hemisphere.SUL: EvapotranspirationDfTable.DF_DATA_SOUTH_SUN_BLANNEY_CRIDDLE()
#     }
#     data = df_data_dict[hemisphere]
#     filtered_df = data[data['latitude'] == latitude]

#     if not filtered_df.empty:
#         if month in filtered_df.columns:
#             rad_value = filtered_df[month.value].iloc[0]
#             return Decimal(str(rad_value))


# def calculate_radiation_blaney_criddle(latitude, hemisphere: Hemispherse, month: MonthEnum):
#     df_data_dict = {
#         Hemispherse.NORTE: EvapotranspirationDfTable.DF_DATA_NORTH_SUN_BLANNEY_CRIDDLE(),
#         Hemispherse.SUL: EvapotranspirationDfTable.DF_DATA_SOUTH_SUN_BLANNEY_CRIDDLE()
#     }
#     data = df_data_dict[hemisphere]
#     filtered_df = data[data['latitude'] == latitude]

#     if not filtered_df.empty:
#         rad_column_name = month
#         return rad_column_name  # Assuming your column names are like 'Jan', 'Fev', etc.
        
#     if rad_column_name in filtered_df.columns:
#             rad_value = filtered_df[rad_column_name].iloc[0]
#             return Decimal(str(rad_value))

def calculate_vapor_saturation_pressure(temperature):
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






