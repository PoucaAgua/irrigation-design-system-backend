from core.tables.dataframes import dataframes


class ConsultNominalDiameterTable:
    data = dataframes.commercial_diameter

    @classmethod
    def nominal_diameter(cls, diameter_calculation):
        if ((diameter_calculation - cls.data["Nominal_Diameter (mm)"]) == 0).any():
            return diameter_calculation

        if diameter_calculation > cls.data["Nominal_Diameter (mm)"].max():
            raise KeyError("Diameter not found in reference tables")

        else:
            index = (cls.data["Nominal_Diameter (mm)"] < diameter_calculation).idxmin()
            return cls.data["Nominal_Diameter (mm)"][index]
