from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)
from core.domain.entity.crop_coefficient_input import CropCoefficientInput


class CropCoefficientService:
    crop_coefficient_repository = CropCoefficientRepository()

    @classmethod
    def upsert_crop_coefficient(cls, crop_coefficient_input: CropCoefficientInput):
        crop_coefficient = cls.crop_coefficient_repository.upsert(crop_coefficient_input)
        return crop_coefficient
