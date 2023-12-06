from sqlalchemy import Column, Integer, String, Float, Boolean
from infrastructure.persistence.models.base import Base


class CropCoefficientModel(Base):
    __tablename__ = "crop_coefficients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    crop_name = Column(String)
    crop_type = Column(String)
    kc_initial = Column(Float)
    kc_mid_season = Column(Float)
    kc_final = Column(Float)
    active = Column(Boolean, default=True)

    def __eq__(self, other: "CropCoefficientModel") -> bool:
        return isinstance(other, self.__class__) and all(
            getattr(self, field_name) == getattr(other, field_name)
            for field_name in self.__dict__.keys()
            if not field_name.startswith("_")
        )
