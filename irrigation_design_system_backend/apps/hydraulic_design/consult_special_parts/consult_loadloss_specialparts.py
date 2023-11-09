from core.tables.load_dataframe import load_dataframes

class ConsultLoadLossSpecialPartsTable:
    
    data = load_dataframes.special_parts

    @classmethod
    def loadloss_special_parts(cls, type, diameter):
        
        sp_load_loss = cls.data.loc[cls.data['Diameter'] == diameter, type].values[0]
        
        return sp_load_loss