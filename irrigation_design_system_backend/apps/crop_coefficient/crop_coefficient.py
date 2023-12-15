from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)

from infrastructure.persistence.session import transactional_session


class CropCoefficientService:
    def __init__(self, repository=None):
        self.crop_repository = repository or CropCoefficientRepository()

    @transactional_session
    def upsert(self, crop_coefficient: CropCoefficientInput):
        if crop_coefficient.id:
            raise ValueError("ID should not be provided, it will be generated automatically")

        new_crop_coefficient = CropCoefficientInput(**crop_coefficient.dict())
        created_id, created_coefficient = self.crop_repository.upsert(new_crop_coefficient)
        return created_id, created_coefficient

    @transactional_session
    def get_all(self):
        return self.crop_repository.get_all()

    @transactional_session
    def get_id(self, crop_coefficient_id):
        if not isinstance(crop_coefficient_id, int) or crop_coefficient_id <= 0:
            raise ValueError("Invalid coefficient ID")

        return self.crop_repository.get_by_id(crop_coefficient_id)

    @transactional_session
    def delete(self, coefficient_id):
        return self.crop_repository.delete(coefficient_id)
