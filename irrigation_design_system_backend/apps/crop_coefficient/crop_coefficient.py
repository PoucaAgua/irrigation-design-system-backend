from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.api.v1.responses.crop_coefficient import CropCoefficientResponse
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)

from infrastructure.persistence.session import transactional_session


class CropCoefficientService:
    crop_repository = CropCoefficientRepository()

    @classmethod
    def upsert(cls, crop_coefficient: CropCoefficientInput) -> CropCoefficientResponse:
        return cls.crop_repository.upsert(crop_coefficient)

    def get_all(self):
        return self.crop_repository.get_all()

    def get_id(self, crop_coefficient_id):
        if not isinstance(crop_coefficient_id, int) or crop_coefficient_id <= 0:
            raise ValueError("Invalid coefficient ID")

        return self.crop_repository.get_by_id(crop_coefficient_id)

    def delete(self, coefficient_id):
        return self.crop_repository.delete(coefficient_id)
