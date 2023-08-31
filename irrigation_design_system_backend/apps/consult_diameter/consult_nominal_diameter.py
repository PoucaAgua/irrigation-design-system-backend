from _decimal import Decimal
from apps.file_reader.source_table import SourceTable

class ConsultNominalDiameterTable:

  data = SourceTable.reference_table_reading("irrigation-design-system-backend/irrigation_design_system_backend/core/files/reference_table_Commercial_diameters.csv")

  def nominal_diameter(self, diameter_calculation):
    
    if ((diameter_calculation - self.data['Nominal_Diameter (mm)']) == 0).any():
      return diameter_calculation

    if diameter_calculation > self.data['Nominal_Diameter (mm)'].max():
      return 'Diameter not found in reference tables'

    else:
      index = (self.data['Nominal_Diameter (mm)'] < diameter_calculation).idxmin()
      return self.data['Nominal_Diameter (mm)'][index]
    