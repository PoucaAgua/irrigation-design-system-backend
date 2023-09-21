import os
from core.tables.read_files import read_file
from enum import Enum

script_dir = os.path.dirname(os.path.abspath(__file__))


def df_data_radiation_hargraves_samani():
    file_path = os.path.join(script_dir, "files/data_radiation_hargreaves_samani.csv")
    return read_file(file_path)


def df_data_north_sun_blanney_criddle():
    file_path = os.path.join(script_dir, "files/data_percent_daily_hours_north_blanney_criddle.csv")
    return read_file(file_path)


def df_data_south_sun_blanney_criddle():
    file_path = os.path.join(script_dir, "files/data_percent_daily_hours_south_blanney_criddle.csv")
    print(file_path)
    return read_file(file_path)


class EvapotranspirationDfTable(Enum):
    DF_RADIATION_HARGRAVES_SAMANI = df_data_radiation_hargraves_samani
    DF_DATA_NORTH_SUN_BLANNEY_CRIDDLE = df_data_north_sun_blanney_criddle
    DF_DATA_SOUTH_SUN_BLANNEY_CRIDDLE = df_data_south_sun_blanney_criddle
