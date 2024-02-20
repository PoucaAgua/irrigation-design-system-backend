from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput
from core.domain.entity.crop_coefficient.crop_coefficient_output import CropCoefficientResponse
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)


class CropCoefficientService:
    crop_repository = CropCoefficientRepository()

    @classmethod
    def upsert(cls, crop_coefficient: CropCoefficientInput) -> CropCoefficientResponse:
        return cls.crop_repository.upsert(crop_coefficient)
