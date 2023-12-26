from http.client import HTTPException
from core.domain.entity.crop_coefficient_input import (
    CropCoefficientInput,
)
from infrastructure.api.v1.responses.crop_coefficient import (
    CropCoefficientResponse,
)
from infrastructure.persistence.models.crop_coefficient import (
    CropCoefficientModel,
)
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)
from infrastructure.persistence.session import SessionLocal


class CropCoefficientService:
    crop_repository = CropCoefficientRepository()

    @classmethod
    def upsert(cls, crop_coefficient: CropCoefficientInput) -> CropCoefficientResponse:
        return cls.crop_repository.upsert(crop_coefficient)

    @classmethod
    def get_all(cls):
        return cls.crop_repository.get_all()

    @classmethod
    def get_id(cls, crop_coefficient_id):
        if not isinstance(crop_coefficient_id, int) or crop_coefficient_id <= 0:
            raise ValueError("Invalid coefficient ID")

        return cls.crop_repository.get_by_id(crop_coefficient_id)

    @classmethod
    def delete(cls, coefficient_id):
        return cls.crop_repository.delete(coefficient_id)

    @classmethod
    def update(
        cls, coefficient_id: int, updated_coefficient: CropCoefficientInput
    ) -> CropCoefficientResponse:
        db = SessionLocal()
        try:
            existing_coefficient = (
                db.query(CropCoefficientModel)
                .filter(CropCoefficientModel.id == coefficient_id)
                .first()
            )

            if existing_coefficient:
                for field, value in updated_coefficient.dict(exclude_unset=True).items():
                    setattr(existing_coefficient, field, value)

                db.add(existing_coefficient)
                db.commit()
                db.refresh(existing_coefficient)
                return existing_coefficient.to_response()

            raise HTTPException(status_code=404, detail="Crop coefficient not found")
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
