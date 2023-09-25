from _decimal import Decimal
from core.domain.enum.month import MonthEnum
from core.tables.dataframes import dataframes
from apps.evapotranspiration.reference_evapotranspiration.interpolate import interpolate
from core.domain.enum.hemisphere import Hemisphere


def calculate_percent_daily_solar_hours(
    latitude: int, month: MonthEnum, hemisphere: Hemisphere
) -> Decimal:
    df_data = dataframes.percent_daily_solar_hours_south
    if hemisphere == Hemisphere.NORTE:
        df_data = dataframes.percent_daily_solar_hours_north

    percent_daily_solar_hours = interpolate(
        df_data["latitude"], df_data[month.value], float(latitude)
    )
    return Decimal(str(percent_daily_solar_hours))
