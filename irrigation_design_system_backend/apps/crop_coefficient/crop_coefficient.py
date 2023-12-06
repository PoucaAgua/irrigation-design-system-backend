from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)


class CropCoefficientService:
    def __init__(self, repository=None):
        self.crop_repository = repository if repository else CropCoefficientRepository()

    def upsert(self, crop_coefficient: CropCoefficientInput):
        if not isinstance(crop_coefficient.id, int) or crop_coefficient.id <= 0:
            raise ValueError("Invalid coefficient ID")

        self.crop_repository.upsert(crop_coefficient)

    def get_all(self, db):
        return self.crop_repository.get_all(db)

    def get_id(self, db, crop_coefficient_id):
        if not isinstance(crop_coefficient_id, int) or crop_coefficient_id <= 0:
            raise ValueError("Invalid coefficient ID")

        return self.crop_repository.get_id(db, crop_coefficient_id)

    def delete(self, coefficient_id):
        return self.crop_repository.delete(coefficient_id)
