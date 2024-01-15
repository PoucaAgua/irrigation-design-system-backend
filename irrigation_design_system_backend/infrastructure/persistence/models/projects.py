from sqlalchemy import Column, String, DECIMAL, ForeignKey, BigInteger, Enum, JSON
from sqlalchemy.orm import relationship

from infrastructure.persistence.models.base import Base
from core.domain.enum.line_types import LineTypes
from core.domain.enum.status_types import StatusTypes


class Project(Base):
    __tablename__ = "projects"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, index=True)
    group_id = Column(String(100))
    description = Column(String(250))
    status = Column(Enum(StatusTypes, name="project_status"))
    crop = Column(String(100))
    maximum_actual_irrigation_required = Column(DECIMAL(10, 2), default=0.00)
    crop_evapotranspiration = Column(DECIMAL(10, 2), default=0.00)
    total_irrigation_required = Column(DECIMAL(10, 2), default=0.00)

    # Foreign Keys
    lateral_line = relationship("LateralLine", back_populates="project", uselist=True)
    derivation_line = relationship("DerivationLine", back_populates="project", uselist=True)

    def __eq__(self, other):
        if isinstance(other, Project):
            return (
                self.id == other.id
                and self.user_id == other.user_id
                and self.group_id == other.group_id
                and self.description == other.description
                and self.crop == other.crop
                and self.maximum_actual_irrigation_required
                == other.maximum_actual_irrigation_required
                and self.crop_evapotranspiration == other.crop_evapotranspiration
                and self.total_irrigation_required == other.total_irrigation_required
                and self.lateral_line == other.lateral_line
                and self.derivation_line == other.derivation_line
            )
        return False


class LateralLine(Base):
    __tablename__ = "lateral_lines"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    project_id = Column(BigInteger, ForeignKey("projects.id"), index=True)
    dripper = Column(String(250))
    decline = Column(DECIMAL(10, 2))
    inlet_pressure = Column(DECIMAL(10, 2))
    separation_between_issuers = Column(DECIMAL(10, 2))
    length_max = Column(DECIMAL(10, 2))
    diameter = Column(DECIMAL(10, 2))
    localized_loss = Column(DECIMAL(10, 2))
    type = Column(Enum(LineTypes, name="lateral_line_types"))

    # Foreign Keys
    project = relationship("Project", back_populates="lateral_line", uselist=False)

    def __eq__(self, other):
        if isinstance(other, LateralLine):
            return (
                self.id == other.id
                and self.project_id == other.project_id
                and self.dripper == other.dripper
                and self.decline == other.decline
                and self.inlet_pressure == other.inlet_pressure
                and self.separation_between_issuers == other.separation_between_issuers
                and self.length_max == other.length_max
                and self.diameter == other.diameter
                and self.localized_loss == other.localized_loss
                and self.type == other.type
            )
        return False


class DerivationLine(Base):
    __tablename__ = "derivation_lines"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    project_id = Column(BigInteger, ForeignKey("projects.id"), index=True)
    pipe_type = Column(String(250))
    inlet_pressure = Column(DECIMAL(10, 2))
    length = Column(JSON)
    diameter = Column(JSON)
    localized_loss = Column(String(250))
    type = Column(Enum(LineTypes, name="derivation_line_types"))

    # Foreign Keys
    project = relationship("Project", back_populates="derivation_line", uselist=False)

    def __eq__(self, other):
        if isinstance(other, DerivationLine):
            return (
                self.id == other.id
                and self.project_id == other.project_id
                and self.pipe_type == other.pipe_type
                and self.inlet_pressure == other.inlet_pressure
                and self.length == other.length
                and self.diameter == other.diameter
                and self.localized_loss == other.localized_loss
                and self.type == other.type
            )
        return False
