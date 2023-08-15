from _decimal import Decimal
from file_reader.source_table import reference_table_reading

class ConsultNominalDiameterTable:

  def nominal_diameter(diameter_calculation:Decimal) -> Decimal:

    data = reference_table_reading("/content/reference_table_Commercial_diameters.csv")

    if ((diameter_calculation - data['Nominal_Diameter (mm)']) == 0).any():
      return diameter_calculation

    if diameter_calculation > data['Nominal_Diameter (mm)'].max():
      return 'Diameter not found in reference tables'

    else:
      index = (data['Nominal_Diameter (mm)'] < diameter_calculation).idxmin()
      return data['Nominal_Diameter (mm)'][index]
    