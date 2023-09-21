from _decimal import Decimal
from core.domain.enum.month import MonthEnum
from core.tables.dataframes import dataframes
from apps.evapotranspiration.interpolate import interpolate


def calculate_radiation_hargreaves_samani(latitude: Decimal, month: MonthEnum):
    df_radiation = dataframes.radiation_hargreaves_samani
    rad_value = interpolate(df_radiation["latitude"], df_radiation[month.value], float(latitude))
    return Decimal(str(rad_value))
