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