from _decimal import Decimal
from core.domain.enum.month import MonthEnum_hargraves
from core.tables.evapotraspiration_tables import EvapotranspirationDfTable
from apps.evapotranspiration.interpolate import interpolate
from core.domain.enum.hemisphere import Hemisphere


def calculate_radiation_blaney_criddle(latitude: Decimal, month: MonthEnum_hargraves, hemisphere):
    df_data_norte = EvapotranspirationDfTable.DF_DATA_NORTH_SUN_BLANNEY_CRIDDLE()
    df_data_sul = EvapotranspirationDfTable.DF_DATA_SOUTH_SUN_BLANNEY_CRIDDLE()

    if hemisphere == Hemisphere.NORTE:
        df_data = df_data_norte
    elif hemisphere == Hemisphere.SUL:
        df_data = df_data_sul

    rad_value = interpolate(
        df_data[month.value], [df_data["latitude"] == latitude].iloc[0], float(latitude)
    )

    return Decimal(str(rad_value))
