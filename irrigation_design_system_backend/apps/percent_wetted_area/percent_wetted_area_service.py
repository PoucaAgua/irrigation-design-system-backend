from _decimal import Decimal
from core.constants.math import MathConstants
from core.domain.entity.PWAEntity import IBTEntity,TSWEntity,CPEntity

class PercentWettedAreaService:

    #Calculation of tree irrigation.
    @classmethod
    def calculate_irrigation_by_tree(cls, ibt_entity: IBTEntity) -> Decimal:
        
        Np = ibt_entity.drippers_number
        Dw = cls.dw_calculate(ibt_entity)
        Sr = ibt_entity.space_between_lines
        Sp = ibt_entity.space_between_plants

        return Decimal(Np * MathConstants.PI * Dw**2  * 100 / (4 * Sp * Sr))

    #Calculation of the maximum wetted diameter by the dripper, m.
    @classmethod
    def dw_calculate(cls, ibt_entity: IBTEntity) -> Decimal:

        Z = ibt_entity.value_of_z
        q = ibt_entity.value_of_q
        K0 = ibt_entity.hydraulic_conductivity_of_saturated_soil

        #return Decimal(1.32 * Z**0.35 * (q / K0)**0.33)  
        return Decimal('1.32') * Z**Decimal('0.35') * (q / K0)**Decimal('0.33')
    
    #Calculation of the saturated wetted radius.
    @classmethod
    def calculate_twice_saturated_wetted_radius(cls,tsw_entity: TSWEntity) -> Decimal:
        
        Alpha = tsw_entity.parameter_model_unsaturated_hydraulic
        K0 = tsw_entity.hydraulic_conductivity_of_saturated_soil
        q = tsw_entity.value_of_q
       
        #return Decimal(2 * ((4 / Alpha**2 * MathConstants.PI**2) + ( q / MathConstants.PI * K0 ) - ( 2 / Alpha * MathConstants.PI ))**0.5)
        return Decimal(2) * ((4 / Alpha**2 * MathConstants.PI**2) + (q / MathConstants.PI * K0) - (2 / Alpha * MathConstants.PI))**Decimal('0.5')

    #Calculation of irrigation to form a continuous strip.
    @classmethod
    def calculate_continuous_strip(cls, cp_entity: CPEntity) -> Decimal:
        
        Aw = cls.moistened_area_calculate(cp_entity)
        Ap = cls.area_occupied_plant_calculate(cp_entity)

        return Decimal(Aw / Ap * 100)
    
    #Calculation of the moistened area.
    def moistened_area_calculate(cp_entity: CPEntity) -> Decimal:

        Sp = cp_entity.space_between_plants
        Sw = cp_entity.wetted_zone

        return (Sp * Sw)
    
    #Calculation of the area occupied by the plant.
    def area_occupied_plant_calculate(cp_entity: CPEntity) -> Decimal:

        Sp = cp_entity.space_between_plants
        Sr = cp_entity.row_spacing_plants 
        
        return (Sp * Sr)
