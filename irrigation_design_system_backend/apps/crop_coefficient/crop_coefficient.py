from pydantic import BaseModel
from decimal import Decimal

from core.domain.entity.crop_coefficient_entity import CropCoefficientEntity
from infrastructure.persistence.repository.crop_coefficient_repository import CropCoefficientRepositoryV2


class CropCoefficientService:

    crop_repository = CropCoefficientRepositoryV2()

    @classmethod
    def upsert(cls, crop_coefficient: CropCoefficientEntity):
        cls.crop_repository.upsert(crop_coefficient)
        return

