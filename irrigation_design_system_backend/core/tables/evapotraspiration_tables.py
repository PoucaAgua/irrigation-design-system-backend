import os
from core.tables.read_files import read_file, read_file_hargraves
import pandas as pd
from enum import Enum
from decimal import Decimal

script_dir = os.path.dirname(os.path.abspath(__file__))


def df_data_radiation_hargraves_samani():
    file_path = os.path.join(script_dir, "files/data_radiation_hargraves_samani.csv")
    return read_file_hargraves(file_path)


def df_data_north_sun_blanney_criddle():
    file_path = os.path.join(script_dir, "files/data_percent_daily_hours_north_blanney_criddle.csv")
    return read_file(file_path)


def df_data_south_sun_blanney_criddle():
    file_path = os.path.join(script_dir, "files/data_percent_daily_hours_south_blanney_criddle.csv")
    return read_file(file_path)


class EvapotranspirationDfTable(Enum):
    DF_RADIATION_HARGRAVES_SAMANI = df_data_radiation_hargraves_samani
    DF_DATA_NORTH_SUN_BLANNEY_CRIDDLE = df_data_north_sun_blanney_criddle
    DF_DATA_SOUTH_SUN_BLANNEY_CRIDDLE = df_data_south_sun_blanney_criddle


def interpolate_value(input_value):
    data = df_data_radiation_hargraves_samani()
    data['latitude s'] = data['latitude s'].replace(',', '.').apply(pd.to_numeric, errors='coerce')
    interpolated_data = data.interpolate(
        method='values', axis=1, limit_direction='both', limit=1
    )
    for column in interpolated_data.columns[1:]:
        interpolated_data[column] = interpolated_data[column].apply(
            lambda x: Decimal(str(x)) if not pd.isna(x) else None
        )

    interpolated_value = None
    for row in interpolated_data.iterrows():
        if input_value >= row['latitude s']:
            interpolated_value = row[1:]
        else:
            break

    return interpolated_value
