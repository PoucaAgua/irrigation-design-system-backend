from core.tables.source_table import SourceTable

class LoadDataframe:

    @classmethod
    def commercial_diameter(self):
        
        data = SourceTable.reference_table_reading("/files/reference_table_Commercial_diameters.csv")
        
        return data