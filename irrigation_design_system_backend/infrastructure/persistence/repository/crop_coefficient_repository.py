from typing import Optional
from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.mappers.crop_coefficient_mapper import CropCoefficientMapper
from infrastructure.persistence.models.crop_coefficient_model import CropCoefficientModel
from infrastructure.persistence.session import transactional_session


class CropCoefficientRepository:
    @transactional_session
    def upsert(self, db, crop_coefficient: CropCoefficientInput) -> CropCoefficientModel:
        crop_coefficient_db = CropCoefficientMapper.entity_to_model(crop_coefficient)

        if crop_coefficient_db.crop_id is None:
            db.add(crop_coefficient_db)
            return crop_coefficient_db

        crop_coefficient_db_persisted = self.get_by_id(db, crop_coefficient_db.crop_id)
        if not crop_coefficient_db_persisted:
            raise ValueError(f"invalid id {crop_coefficient_db.crop_id}")

        crop_coefficient_db = CropCoefficientMapper.entity_to_model_persisted(
            crop_coefficient, crop_coefficient_db_persisted
        )
        db.merge(crop_coefficient_db)
        return crop_coefficient_db

    @staticmethod
    def get_by_id(db, crop_id: int) -> Optional[CropCoefficientModel]:
        return (
            db.query(CropCoefficientModel).filter(CropCoefficientModel.crop_id == crop_id).first()
        )
