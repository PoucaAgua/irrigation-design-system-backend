import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)

from irrigation_design_system_backend.infrastructure.persistence.session import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# banco de dados de teste
def create_test_db():
    def _setup():
        engine = create_engine("sqlite:///./test_sql_app.db")
        SessionLocal.configure(bind=engine)
        return engine

    def _teardown():
        engine.dispose()

    return _setup, _teardown


#  criar e limpar o banco de dados de teste
setup_test_db, teardown_test_db = create_test_db()


@pytest.fixture
def test_db(setup_test_db, teardown_test_db):
    setup, teardown = setup_test_db(), teardown_test_db()
    yield setup
    teardown


class TestCropCoefficientRepository:
    @pytest.fixture(autouse=True)
    def setup(self, test_db):
        self.repository = CropCoefficientRepository()

    def test_upsert_new_coefficient(self, test_db):
        # inserção de um novo coeficiente de cultivo
        coefficient = CropCoefficientInput(
            crop_name="CropA",
            crop_type="TypeA",
            kc_initial=0.5,
            kc_mid_season=1.0,
            kc_final=1.5,
            active=True,
        )
        self.repository.upsert(test_db, coefficient)

        # se foi inserido corretamente
        retrieved = self.repository.get_all(test_db)
        assert len(retrieved) == 1
        assert retrieved[0].crop_name == "CropA"

    def test_upsert_existing_coefficient(self, test_db):
        # Atualização de um coeficiente existente
        coefficient = CropCoefficientInput(
            crop_name="CropB",
            crop_type="TypeB",
            kc_initial=0.7,
            kc_mid_season=1.2,
            kc_final=1.8,
            active=True,
        )

        self.repository.upsert(test_db, coefficient)

        updated_coefficient = CropCoefficientInput(
            id=1,
            crop_name="UpdatedCrop",
            crop_type="UpdatedType",
            kc_initial=0.8,
            kc_mid_season=1.4,
            kc_final=2.0,
            active=True,
        )
        self.repository.upsert(test_db, updated_coefficient)

        # Verificar se o coeficiente foi atualizado corretamente
        retrieved = self.repository.get_id(test_db, 1)
        assert retrieved.crop_name == "UpdatedCrop"

    def test_get_all(self, test_db):
        # Testar obter todos os coeficientes
        coefficient_1 = CropCoefficientInput(
            crop_name="CropC",
            crop_type="TypeC",
            kc_initial=0.6,
            kc_mid_season=1.0,
            kc_final=1.4,
            active=True,
        )
        coefficient_2 = CropCoefficientInput(
            crop_name="CropD",
            crop_type="TypeD",
            kc_initial=0.8,
            kc_mid_season=1.2,
            kc_final=1.6,
            active=True,
        )
        self.repository.upsert(test_db, coefficient_1)
        self.repository.upsert(test_db, coefficient_2)

        # Verificar se todos os coeficientes foram obtidos corretamente
        all_coefficients = self.repository.get_all(test_db)
        assert len(all_coefficients) == 2
        assert all_coefficients[0].crop_name == "CropC"
        assert all_coefficients[1].crop_name == "CropD"

    def test_get_id(self, test_db):
        # Testar obter um coeficiente por ID
        coefficient = CropCoefficientInput(
            crop_name="CropE",
            crop_type="TypeE",
            kc_initial=0.7,
            kc_mid_season=1.1,
            kc_final=1.5,
            active=True,
        )
        self.repository.upsert(test_db, coefficient)

        retrieved_id = self.repository.get_all(test_db)[0].id

        # Verificar se o coeficiente foi obtido corretamente pelo ID
        retrieved = self.repository.get_id(test_db, retrieved_id)
        assert retrieved.crop_name == "CropE"
