from fastapi import HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from apps.crop_coefficient.crop_coefficient import CropCoefficientData

Base = declarative_base()


class CropCoefficientModel(Base):
    __tablename__ = "crop_coefficients"

    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String, index=True)
    crop_type = Column(String)
    kc_initial = Column(Float)
    kc_mid_season = Column(Float)
    kc_final = Column(Float)
    active = Column(Boolean, default=True)


engine = create_engine("sqlite:///sql_app.db")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def crop_coefficient_post(cropcoefficient: CropCoefficientData, active: bool = True):
    db_cropcoefficient = CropCoefficientModel(
        crop_name=cropcoefficient.crop_name,
        crop_type=cropcoefficient.crop_type,
        kc_initial=cropcoefficient.kc_initial,
        kc_mid_season=cropcoefficient.kc_mid_season,
        kc_final=cropcoefficient.kc_final,
        active=active,
    )
    session = Session()
    session.add(db_cropcoefficient)
    session.commit()
    session.refresh(db_cropcoefficient)
    session.close()
    return db_cropcoefficient


def crop_coefficient_get_id(get_id: int):
    session = Session()
    db_cropcoefficient = (
        session.query(CropCoefficientModel).filter(CropCoefficientModel.id == get_id).first()
    )
    session.close()
    return db_cropcoefficient


def crop_coefficients_get_all():
    session = Session()
    crop_coefficients = session.query(CropCoefficientModel).all()
    session.close()
    return crop_coefficients


def crop_coefficient_active(get_id: int, active: bool):
    session = Session()
    db_cropcoefficient = (
        session.query(CropCoefficientModel).filter(CropCoefficientModel.id == get_id).first()
    )
    if db_cropcoefficient:
        db_cropcoefficient.active = active
        session.commit()
        return db_cropcoefficient
    else:
        session.close()
        raise HTTPException(status_code=404, detail="Recurso não encontrado")


def crop_coefficient_update(get_id: int, update_data: CropCoefficientData):
    session = Session()
    db_cropcoefficient = (
        session.query(CropCoefficientModel).filter(CropCoefficientModel.id == get_id).first()
    )
    if db_cropcoefficient:
        db_cropcoefficient.crop_name = update_data.crop_name
        db_cropcoefficient.crop_type = update_data.crop_type
        db_cropcoefficient.kc_initial = update_data.kc_initial
        db_cropcoefficient.kc_mid_season = update_data.kc_mid_season
        db_cropcoefficient.kc_final = update_data.kc_final
        session.commit()
        session.close()
    else:
        session.close()
        raise HTTPException(status_code=404, detail="Recurso não encontrado")


def crop_coefficient_delete(get_id: int):
    session = Session()
    db_cropcoefficient = (
        session.query(CropCoefficientModel).filter(CropCoefficientModel.id == get_id).first()
    )
    if db_cropcoefficient:
        session.delete(db_cropcoefficient)
        session.commit()
        session.close()
    else:
        session.close()
        raise HTTPException(status_code=404, detail="Recurso não encontrado")
