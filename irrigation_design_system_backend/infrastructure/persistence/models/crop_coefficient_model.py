from sqlalchemy import Column, Integer, String, Float, Boolean
from infrastructure.persistence.models.base import Base
from infrastructure.api.v1.responses.crop_coefficient_responses import CropCoefficientResponse


class CropCoefficientModel(Base):
    __tablename__ = "crop_coefficients"

    crop_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    crop_name = Column(String)
    crop_type = Column(String)
    kc_initial = Column(Float)
    kc_mid_season = Column(Float)
    kc_final = Column(Float)
    is_active = Column(Boolean, default=True)

    def __eq__(self, other: "CropCoefficientModel") -> bool:
        return isinstance(other, self.__class__) and all(
            getattr(self, field_name) == getattr(other, field_name)
            for field_name in self.__dict__.keys()
            if not field_name.startswith("_")
        )

    def to_response(self) -> "CropCoefficientResponse":
        return CropCoefficientResponse(
            crop_id=self.crop_id,
            crop_name=self.crop_name,
            crop_type=self.crop_type,
            kc_initial=self.kc_initial,
            kc_mid_season=self.kc_mid_season,
            kc_final=self.kc_final,
            is_active=self.is_active,
        )
