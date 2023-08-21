from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, BigInteger, Enum, JSON
from sqlalchemy.orm import relationship

from infrastructure.persistence.models.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, index=True)
    group_id = Column(String(100))
    description = Column(String(250))
    status = Column(String(100))
    crop = Column(String(100))
    maximum_actual_irrigation_required = Column(DECIMAL(10, 2), default=0.00)
    crop_evapotranspiration = Column(DECIMAL(10, 2), default=0.00)
    total_irrigation_required = Column(DECIMAL(10, 2), default=0.00)

    # Foreign Keys
    lateral_line = relationship('LateralLine', back_populates='project', uselist=True)
    derivation_line = relationship('DerivationLine', back_populates='project', uselist=True)


class LateralLine(Base):
    __tablename__ = "lateral_lines"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    project_id = Column(BigInteger, ForeignKey('projects.id'), index=True)
    dripper = Column(String(250))
    declive = Column(DECIMAL(10, 2))
    inlet_pressure = Column(DECIMAL(10, 2))
    separation_between_issuers = Column(DECIMAL(10, 2))
    length_max = Column(DECIMAL(10, 2))
    diameter = Column(DECIMAL(10, 2))
    localized_loss = Column(DECIMAL(10, 2))
    type = Column(Enum('with_plc', 'without_plc'))

    # Foreign Keys
    project = relationship('Project', back_populates='lateral_line', uselist=False)


class DerivationLine(Base):
    __tablename__ = "derivation_lines"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    project_id = Column(BigInteger, ForeignKey('projects.id'), index=True)
    pipe_type = Column(String(250))
    inlet_pressure = Column(DECIMAL(10, 2))
    length = Column(JSON)
    diameter = Column(JSON)
    localized_loss = Column(String(250))
    type = Column(Enum('with_plc', 'without_plc'))

    # Foreign Keys
    project = relationship('Project', back_populates='derivation_line', uselist=False)
