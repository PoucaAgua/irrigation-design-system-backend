from sqlalchemy import Column, Integer, String, Float, Boolean
from infrastructure.persistence.models.base import Base


class CropCoefficientModel(Base):
    __tablename__ = "crop_coefficients"

    crop_id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String(100))
    crop_type = Column(String(100))
    kc_initial = Column(Float)
    kc_mid_season = Column(Float)
    kc_final = Column(Float)
    is_active = Column(Boolean, default=True)
