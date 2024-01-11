from typing import List

from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput
from infrastructure.api.v1.responses.crop_coefficient_responses import CropCoefficientResponse
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)
from infrastructure.persistence.session import get_db

from infrastructure.persistence.mappers.crop_coefficient_mapper import CropCoefficientMapper


class CropCoefficientService:
    crop_repository = CropCoefficientRepository()

    @classmethod
    def upsert(cls, crop_coefficient: CropCoefficientInput) -> CropCoefficientResponse:
        return cls.crop_repository.upsert(crop_coefficient)

    @classmethod
    def get_all(cls) -> List[CropCoefficientResponse]:
        with get_db() as db:
            crop_coefficients = cls.crop_repository.get_all(db)
            return [CropCoefficientMapper.to_response(crop) for crop in crop_coefficients]

    @classmethod
    def get_id(cls, crop_coefficient_id):
        if not isinstance(crop_coefficient_id, int) or crop_coefficient_id <= 0:
            raise ValueError("Invalid coefficient ID")

        db = get_db()

        try:
            return cls.crop_repository.get_by_id(db, crop_coefficient_id)
        finally:
            db.close()
