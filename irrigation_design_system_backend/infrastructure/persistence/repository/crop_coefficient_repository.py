from typing import Optional, List
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.mappers.crop_coefficient import CropCoefficientMapper
from infrastructure.persistence.models.crop_coefficient import CropCoefficientModel
from infrastructure.persistence.session import transactional_session
from sqlalchemy import func


class CropCoefficientRepository:
    @transactional_session
    def upsert(self, db, crop_coefficient: CropCoefficientInput) -> CropCoefficientModel:
        crop_coefficient_db = CropCoefficientMapper.entity_to_model(crop_coefficient)

        if crop_coefficient_db.id is None:
            last_id = db.query(func.max(CropCoefficientModel.id)).scalar() or 0
            new_id = last_id + 1
            crop_coefficient_db.id = new_id

        if crop_coefficient_db.id:
            crop_coefficient_persisted = self.__get_by_id(db, crop_coefficient_db.id)
            if not crop_coefficient_persisted:
                raise FileNotFoundError(f"Invalid ID {crop_coefficient_db.id}")

        db.add(crop_coefficient_db)
        return crop_coefficient_db

    @staticmethod
    def __get_by_id(db, _id: int) -> Optional[CropCoefficientModel]:
        return db.query(CropCoefficientModel).filter(CropCoefficientModel.id == _id).first()

    @transactional_session
    def get_all(self, db) -> List[CropCoefficientModel]:
        return db.query(CropCoefficientModel).all()

    @transactional_session
    def get_by_id(self, db, _id: int) -> Optional[CropCoefficientModel]:
        return db.query(CropCoefficientModel).filter(CropCoefficientModel.id == _id).first()
