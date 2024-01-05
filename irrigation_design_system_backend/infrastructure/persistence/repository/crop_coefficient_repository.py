from typing import Optional, List
from infrastructure.persistence.mappers.crop_coefficient_mapper import CropCoefficientMapper
from infrastructure.persistence.session import transactional_session
from infrastructure.persistence.models.crop_coefficient_model import CropCoefficientModel

from core.domain.entity.crop_coefficient_input import CropCoefficientInput


class CropCoefficientRepository:
    @transactional_session
    def upsert(self, db, crop_coefficient_input: CropCoefficientInput) -> CropCoefficientModel:
        crop_coefficient_db = CropCoefficientMapper.model_from_input(crop_coefficient_input)

        if crop_coefficient_db.crop_id is not None:
            crop_coefficient_db_persisted = self.__get_by_id(db, crop_coefficient_db.crop_id)
            if crop_coefficient_db_persisted:
                crop_coefficient_db = CropCoefficientMapper.model_from_input_and_persisted(
                    crop_coefficient_input, crop_coefficient_db_persisted
                )
                db.merge(crop_coefficient_db)
                return crop_coefficient_db

        db.add(crop_coefficient_db)
        return crop_coefficient_db

    @transactional_session
    def get_by_id(self, db, _id: int) -> Optional[CropCoefficientModel]:
        return self.__get_by_id(db, _id)

    @staticmethod
    def __get_by_id(db, _id: int) -> Optional[CropCoefficientModel]:
        return db.query(CropCoefficientModel).filter(CropCoefficientModel.crop_id == _id).first()

    @transactional_session
    def get_all(self, db) -> List[CropCoefficientModel]:
        return db.query(CropCoefficientModel).all()
