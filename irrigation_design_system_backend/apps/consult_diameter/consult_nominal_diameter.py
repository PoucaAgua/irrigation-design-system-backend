from core.tables.load_dataframe import LoadDataframe

class ConsultNominalDiameterTable:

  data = LoadDataframe.commercial_diameter()

  @classmethod
  def nominal_diameter(cls, diameter_calculation):
    
    if ((diameter_calculation - cls.data['Nominal_Diameter (mm)']) == 0).any():
      return diameter_calculation

    if diameter_calculation > cls.data['Nominal_Diameter (mm)'].max():
      return 'Diameter not found in reference tables'

    else:
      index = (cls.data['Nominal_Diameter (mm)'] < diameter_calculation).idxmin()
      return cls.data['Nominal_Diameter (mm)'][index]
    