from core.tables.source_table import SourceTable


class Dataframes:
    PATH = "/files/"
    COMMERCIAL_DIAMETER_PATH = PATH + "reference_table_commercial_diameters.csv"

    def __init__(self):
        self._commercial_diameter = None

    @property
    def commercial_diameter(self):
        if self._commercial_diameter:
            return self._commercial_diameter

        self._commercial_diameter = SourceTable.reference_table_reading(
            self.COMMERCIAL_DIAMETER_PATH
        )
        return self._commercial_diameter


dataframes = Dataframes()
