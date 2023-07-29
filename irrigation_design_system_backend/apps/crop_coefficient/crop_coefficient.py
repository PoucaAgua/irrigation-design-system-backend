from _decimal import Decimal

from core.domain.entity.cropcoefficient import CropCoefficientEntity
from infrastructure.persistence.repository.crop_coefficient import CropCoefficient


class CropCoefficient:
    
    @staticmethod
    def constants_crop_coefficient(entity: CropCoefficientEntity) -> Decimal:
        
