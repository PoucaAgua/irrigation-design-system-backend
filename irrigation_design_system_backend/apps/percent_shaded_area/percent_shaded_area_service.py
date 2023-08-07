from _decimal import Decimal
from core.constants.math import MathConstants
from core.domain.entity.PSAEntity import SAEntity,CPEntity

class PercentShadedAreaService:


    #Calculation of the diameter of the plant's canopy projection.
    @classmethod
    def calculate_shaded_area(cls, sa_entity: SAEntity) -> Decimal:
     
        Dco = sa_entity.diameter_of_the_plants_canopy_projection
        Sp = sa_entity.space_between_plants
        Sr = sa_entity.strip_shaded_by_the_plant

        return Decimal( MathConstants.PI * (Dco**2 / 4) / (Sr * Sp) )
    
    #Calculation of shaded strip by the plant.
    @classmethod
    def calculate_crop_projection(cls, cp_entity: CPEntity) -> Decimal:
     
        Ss = cp_entity.shaded_strip_plant
        Sr = cp_entity.strip_shaded_by_the_plant

        return Decimal( Ss / Sr )
    
        

       