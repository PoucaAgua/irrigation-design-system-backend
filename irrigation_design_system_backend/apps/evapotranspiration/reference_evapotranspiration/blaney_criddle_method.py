from _decimal import Decimal
from core.domain.enum.month import MonthEnum
from core.tables.dataframes import dataframes
from apps.evapotranspiration.interpolate import interpolate
from core.domain.enum.hemisphere import Hemisphere


def calculate_percent_daily_hours(latitude: int, month: MonthEnum, hemisphere):
    df_north = dataframes.percent_daily_hours_north
    df_south = dataframes.percent_daily_hours_south
    df_data = df_north if hemisphere == Hemisphere.NORTE else df_south

    rad_value = interpolate(df_data["latitude"], df_data[month.value], float(latitude))

    return Decimal(str(rad_value))
