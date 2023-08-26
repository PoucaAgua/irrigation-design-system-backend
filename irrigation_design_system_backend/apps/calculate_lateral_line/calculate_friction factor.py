from _decimal import Decimal

from calculate_reynolds import ReynoldsCalculate
from core.domain.entity.lateral_line_entity import ReynoldsNumber
from core.constants.lateral_line import FrictorFactorConstants

class FrictionFactor:

    @staticmethod
    def calculate_friction_factor() -> Decimal:

        reynolds_number = ReynoldsCalculate.calculate_reynolds()

        if reynolds_number < 2000:
            return Decimal(64 / reynolds_number)
        
        elif 2000 < reynolds_number <= 3000: # Verificar intervalo
            return FrictorFactorConstants.transition_factor
        
        elif 3000 < reynolds_number < 100000:
            return FrictorFactorConstants.c / (reynolds_number)**(FrictorFactorConstants.m)
        else:
            return 'Invalid Number'
