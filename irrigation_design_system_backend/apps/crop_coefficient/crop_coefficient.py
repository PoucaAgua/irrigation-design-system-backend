from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)


class CropCoefficientService:
    crop_repository = CropCoefficientRepository()

    @classmethod
    def upsert(cls, crop_coefficient: CropCoefficientInput):
        cls.crop_repository.upsert(crop_coefficient)
        return

    @classmethod
    def get_all(cls, db):
        return cls.crop_repository.get_all(db)

    @classmethod
    def get_id(cls, db, crop_coefficient_id):
        return cls.crop_repository.get_id(db, crop_coefficient_id)
