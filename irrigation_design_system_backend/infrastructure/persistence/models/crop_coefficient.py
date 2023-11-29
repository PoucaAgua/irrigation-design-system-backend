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
        return (
            isinstance(other, self.__class__)
            and self.id == other.id
            and self.crop_name == other.crop_name
            and self.crop_type == other.crop_type
            and self.kc_initial == other.kc_initial
            and self.kc_mid_season == other.kc_mid_season
            and self.kc_final == other.kc_final
            and self.active == other.active
        )
