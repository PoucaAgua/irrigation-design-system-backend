from typing import Optional, List

from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput
from infrastructure.api.v1.responses.crop_coefficient_responses import CropCoefficientResponse
from infrastructure.persistence.mappers.crop_coefficient_mapper import CropCoefficientMapper
from infrastructure.persistence.models.crop_coefficient_model import CropCoefficientModel
from infrastructure.persistence.session import transactional_session


class CropCoefficientRepository:
    @transactional_session
    def upsert(self, db, crop_coefficient: CropCoefficientInput) -> CropCoefficientResponse:
        crop_coefficient_db = self.get_by_id(db, crop_coefficient.crop_id)

        if crop_coefficient_db is None:
            crop_coefficient_db = CropCoefficientMapper.entity_to_model(crop_coefficient)
            db.add(crop_coefficient_db)
        else:
            CropCoefficientMapper.update_model_from_entity(crop_coefficient_db, crop_coefficient)

        db.commit()
        return CropCoefficientMapper.to_response(crop_coefficient_db)

    @staticmethod
    def get_by_id(db, crop_id: int) -> Optional[CropCoefficientModel]:
        return (
            db.query(CropCoefficientModel).filter(CropCoefficientModel.crop_id == crop_id).first()
        )

    @transactional_session
    def get_all(self, db) -> List[CropCoefficientModel]:
        return db.query(CropCoefficientModel).all()
