from typing import List, Optional
from sqlalchemy.orm import Session

from core.domain.entity.crop_coefficient_entity import CropCoefficientEntity
from infrastructure.persistence import models
from infrastructure.persistence.mappers.crop_coefficient import CropCoefficientMapper
from infrastructure.persistence.session import transactional_session


class CropCoefficientRepositoryV2:
    @transactional_session
    def upsert(self, db, crop_coefficient: CropCoefficientEntity):
        crop_coefficient_db = CropCoefficientMapper.entity_to_model(crop_coefficient)
        if crop_coefficient_db.id is None:
            db.add(crop_coefficient_db)
        else:
            db.merge(crop_coefficient_db)

class CropCoefficientRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_crop_coefficient(
        self,
        crop_name: str,
        crop_type: str,
        kc_initial: float,
        kc_mid_season: float,
        kc_final: float,
    ) -> models.CropCoefficientModel:
        db_crop_coefficient = models.CropCoefficientModel(
            crop_name=crop_name,
            crop_type=crop_type,
            kc_initial=kc_initial,
            kc_mid_season=kc_mid_season,
            kc_final=kc_final,
        )
        self.session.add(db_crop_coefficient)
        self.session.commit()
        self.session.refresh(db_crop_coefficient)
        return db_crop_coefficient

    def get_crop_coefficient(
        self, crop_coefficient_id: int
    ) -> Optional[models.CropCoefficientModel]:
        return (
            self.session.query(models.CropCoefficientModel)
            .filter(models.CropCoefficientModel.id == crop_coefficient_id)
            .first()
        )

    def get_all_crop_coefficients(self) -> List[models.CropCoefficientModel]:
        return self.session.query(models.CropCoefficientModel).all()

    def update_crop_coefficient(
        self,
        crop_coefficient_id: int,
        crop_name: str,
        crop_type: str,
        kc_initial: float,
        kc_mid_season: float,
        kc_final: float,
    ) -> Optional[models.CropCoefficientModel]:
        db_crop_coefficient = self.get_crop_coefficient(crop_coefficient_id)
        if db_crop_coefficient:
            db_crop_coefficient.crop_name = crop_name
            db_crop_coefficient.crop_type = crop_type
            db_crop_coefficient.kc_initial = kc_initial
            db_crop_coefficient.kc_mid_season = kc_mid_season
            db_crop_coefficient.kc_final = kc_final
            self.session.commit()
        return db_crop_coefficient

    def delete_crop_coefficient(self, crop_coefficient_id: int) -> bool:
        db_crop_coefficient = self.get_crop_coefficient(crop_coefficient_id)
        if db_crop_coefficient:
            self.session.delete(db_crop_coefficient)
            self.session.commit()
            return True
        return False
