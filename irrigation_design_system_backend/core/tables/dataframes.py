from core.tables.source_table import SourceTable


class Dataframes:
    PATH = "/files/"
    COMMERCIAL_DIAMETER_PATH = PATH + "reference_table_commercial_diameters.csv"
    RADIATION_HARGREAVES_SAMANI_PATH = PATH + "data_radiation_hargreaves_samani.csv"
    PERCENT_DAILY_HOURS_NORTH_PATH = PATH + "data_percent_daily_hours_north_blanney_criddle.csv"
    PERCENT_DAILY_HOURS_SOUTH_PATH = PATH + "data_percent_daily_hours_south_blanney_criddle.csv"

    def __init__(self):
        self._commercial_diameter = None
        self._radiation_hargreaves_samani = None
        self._percent_daily_hours_north = None
        self._percent_daily_hours_south = None

    @property
    def commercial_diameter(self):
        if self._commercial_diameter:
            return self._commercial_diameter

        self._commercial_diameter = SourceTable.reference_table_reading(
            self.COMMERCIAL_DIAMETER_PATH
        )
        return self._commercial_diameter

    @property
    def radiation_hargreaves_samani(self):
        if self._radiation_hargreaves_samani is None:
            self._radiation_hargreaves_samani = SourceTable.reference_table_reading(
                self.RADIATION_HARGREAVES_SAMANI_PATH, delimiter=";", decimal=","
            )
        return self._radiation_hargreaves_samani

    @property
    def percent_daily_hours_north(self):
        if self._percent_daily_hours_north is None:
            self._percent_daily_hours_north = SourceTable.reference_table_reading(
                self.PERCENT_DAILY_HOURS_NORTH_PATH, delimiter=";", decimal=","
            )
        return self._percent_daily_hours_north

    @property
    def percent_daily_hours_south(self):
        if self._percent_daily_hours_south is None:
            self._percent_daily_hours_south = SourceTable.reference_table_reading(
                self.PERCENT_DAILY_HOURS_SOUTH_PATH, delimiter=";", decimal=","
            )
        return self._percent_daily_hours_south


dataframes = Dataframes()
