from sqlalchemy import Column, Integer, String, Float, Boolean
from infrastructure.persistence.models.base import Base


class CropCoefficientModel(Base):
    __tablename__ = "crop_coefficients"

    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String, index=True)
    crop_type = Column(String)
    kc_initial = Column(Float)
    kc_mid_season = Column(Float)
    kc_final = Column(Float)
    active = Column(Boolean, default=True)
