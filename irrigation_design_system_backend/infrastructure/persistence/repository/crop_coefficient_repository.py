from typing import Optional, List
from core.domain.entity.crop_coefficient_input import (
    CropCoefficientInput,
)
from infrastructure.api.v1.responses.crop_coefficient import (
    CropCoefficientResponse,
)
from infrastructure.persistence.mappers.crop_coefficient import (
    CropCoefficientMapper,
)
from infrastructure.persistence.models.crop_coefficient import (
    CropCoefficientModel,
)
from infrastructure.persistence.session import (
    transactional_session,
)


class CropCoefficientRepository:
    @transactional_session
    def upsert(self, db, crop_coefficient: CropCoefficientInput) -> CropCoefficientResponse:
        crop_coefficient_db = CropCoefficientMapper.entity_to_model(crop_coefficient)

        if crop_coefficient_db.id is None:
            db.add(crop_coefficient_db)
        else:
            existing_coefficient = self.__get_by_id(db, crop_coefficient_db.id)

            if existing_coefficient:
                for attr, value in crop_coefficient_db.__dict__.items():
                    setattr(existing_coefficient, attr, value)
                crop_coefficient_db = existing_coefficient
            else:
                raise ValueError(f"Invalid id {crop_coefficient_db.id}")

        db.commit()
        db.refresh(crop_coefficient_db)

        return crop_coefficient_db.to_response()

    @staticmethod
    def __get_by_id(db, _id: int) -> Optional[CropCoefficientModel]:
        return db.query(CropCoefficientModel).filter(CropCoefficientModel.id == _id).first()

    @transactional_session
    def get_all(self, db) -> List[CropCoefficientModel]:
        return db.query(CropCoefficientModel).all()

    @transactional_session
    def get_by_id(self, db, _id: int) -> Optional[CropCoefficientModel]:
        return db.query(CropCoefficientModel).filter(CropCoefficientModel.id == _id).first()

    @transactional_session
    def delete(self, db, coefficient_id: int) -> bool:
        coefficient = self.__get_by_id(db, coefficient_id)

        if coefficient:
            db.delete(coefficient)
            db.commit()
            return True
        return False

    @transactional_session
    def update(
        self, db, coefficient_id: int, updated_data: CropCoefficientInput
    ) -> Optional[CropCoefficientModel]:
        coefficient = (
            db.query(CropCoefficientModel).filter(CropCoefficientModel.id == coefficient_id).first()
        )
        if coefficient:
            updated_fields = updated_data.dict(exclude_unset=True)
            for field, value in updated_fields.items():
                setattr(coefficient, field, value)
            db.commit()
            db.refresh(coefficient)
            return coefficient
        return None
