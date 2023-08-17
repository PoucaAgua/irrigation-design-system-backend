from _decimal import Decimal
from apps.file_reader.source_table import SourceTable

class ConsultNominalDiameterTable:

  def nominal_diameter(diameter_calculation):

    data = SourceTable.reference_table_reading("/home/lucascaue/Área de trabalho/irrigation-design-system-backend/irrigation_design_system_backend/core/files/reference_table_Commercial_diameters.csv")

    if ((diameter_calculation - data['Nominal_Diameter (mm)']) == 0).any():
      return diameter_calculation

    if diameter_calculation > data['Nominal_Diameter (mm)'].max():
      return 'Diameter not found in reference tables'

    else:
      index = (data['Nominal_Diameter (mm)'] < diameter_calculation).idxmin()
      return data['Nominal_Diameter (mm)'][index]
    