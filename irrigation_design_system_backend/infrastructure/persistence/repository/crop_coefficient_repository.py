from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.mappers.crop_coefficient import CropCoefficientMapper
from infrastructure.persistence.models import CropCoefficientModel
from infrastructure.persistence.session import transactional_session


class CropCoefficientRepository:
    @transactional_session
    def upsert(self, db, crop_coefficient: CropCoefficientInput):
        if crop_coefficient.id is None:
            crop_coefficient_db = CropCoefficientMapper.entity_to_model(crop_coefficient)
            db.add(crop_coefficient_db)
        else:
            crop_coefficient_persisted = self.__get_by_id(db, crop_coefficient.id)
            if not crop_coefficient_persisted:
                raise FileNotFoundError(f"invalid id {crop_coefficient.id}")

            crop_coefficient_db = CropCoefficientMapper.entity_to_model_persisted(
                crop_coefficient, crop_coefficient_persisted
            )
            db.merge(crop_coefficient_db)

    @staticmethod
    def __get_by_id(db, _id: int) -> CropCoefficientModel:
        return db.query(CropCoefficientModel).filter(CropCoefficientModel.id == _id).first()




