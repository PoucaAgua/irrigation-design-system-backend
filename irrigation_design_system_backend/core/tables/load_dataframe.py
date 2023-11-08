from core.tables.source_table import SourceTable


class LoadDataframe:

    @property
    def commercial_diameter(self):
        data = SourceTable.reference_table_reading("/files/reference_table_Commercial_diameters.csv")
        return data
    
    @property
    def special_parts(self):
        data = SourceTable.reference_table_reading("/files/special_parts_table.csv")
        return data


load_dataframes = LoadDataframe()
