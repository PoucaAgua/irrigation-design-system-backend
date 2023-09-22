from _decimal import Decimal
from core.domain.enum.month import MonthEnum
from core.tables.dataframes import dataframes
from apps.evapotranspiration.reference_evapotranspiration.interpolate import interpolate


def calculate_solar_radiation(latitude: Decimal, month: MonthEnum) -> Decimal:
    df_radiation = dataframes.solar_radiation
    rad_value = interpolate(df_radiation["latitude"], df_radiation[month.value], float(latitude))
    return Decimal(str(rad_value))
