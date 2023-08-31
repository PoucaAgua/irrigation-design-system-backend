import os
from _decimal import Decimal
from pathlib import Path

from core.tables.source_table import SourceTable


class ConsultNominalDiameterTable:

  data = SourceTable.reference_table_reading("/files/reference_table_Commercial_diameters.csv")

  @classmethod
  def nominal_diameter(cls, diameter_calculation):
    
    if ((diameter_calculation - cls.data['Nominal_Diameter (mm)']) == 0).any():
      return diameter_calculation

    if diameter_calculation > cls.data['Nominal_Diameter (mm)'].max():
      return 'Diameter not found in reference tables'

    else:
      index = (cls.data['Nominal_Diameter (mm)'] < diameter_calculation).idxmin()
      return cls.data['Nominal_Diameter (mm)'][index]
    