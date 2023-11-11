from core.tables.dataframes import dataframes

class ConsultLoadLossSpecialPartsTable:
    
    data = dataframes.special_parts

    @classmethod
    def loadloss_special_parts(cls, type, diameter):

        if diameter not in cls.data['Diameter'].values:
            raise ValueError('Diameter not found in reference tables')
        
        if type not in cls.data.columns:
            raise ValueError('Special part not found in reference tables')
            
        sp_load_loss = cls.data.loc[cls.data['Diameter'] == diameter, type].values[0]
        
        return sp_load_loss