import pytest
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)
from irrigation_design_system_backend.apps.crop_coefficient.crop_coefficient import (
    CropCoefficientService,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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


# criar e limpar o banco de dados de teste antes e depois dos testes
setup_test_db, teardown_test_db = create_test_db()


@pytest.fixture
def test_db(setup_test_db, teardown_test_db):
    setup, teardown = setup_test_db(), teardown_test_db()
    yield setup
    teardown


class TestCropCoefficientService:
    @pytest.fixture(autouse=True)
    def setup(self, test_db):
        self.service = CropCoefficientService()
        self.repo = CropCoefficientRepository()

    def test_upsert(self, test_db):
        # inserir um novo coeficiente de cultivo
        crop_coefficient = CropCoefficientInput(
            crop_name="CropA",
            crop_type="TypeA",
            kc_initial=0.5,
            kc_mid_season=1.0,
            kc_final=1.5,
            active=True,
        )
        self.service.upsert(crop_coefficient)

        # Verifica se o coeficiente foi inserido corretamente
        retrieved = self.repo.get_all(test_db)
        assert len(retrieved) == 1
        assert retrieved[0].crop_name == "CropA"

        # Teste para atualizar um coeficiente de cultivo existente
        crop_coefficient.id = retrieved[0].id
        crop_coefficient.crop_name = "UpdatedCropA"
        self.service.upsert(crop_coefficient)

        # Verifica se o coeficiente foi atualizado corretamente
        updated = self.repo.get_id(test_db, retrieved[0].id)
        assert updated.crop_name == "UpdatedCropA"

        # Inserir um coeficiente com ID inválido (deve falhar)
        invalid_id = CropCoefficientInput(
            id=100,
            crop_name="InvalidCrop",
            crop_type="InvalidType",
            kc_initial=0.3,
            kc_mid_season=0.6,
            kc_final=0.9,
            active=True,
        )
        with pytest.raises(FileNotFoundError):
            self.service.upsert(invalid_id)

    def test_get_all(self, test_db):
        # Obter todos osss coeficientes de cultivo
        crop_coefficient_1 = CropCoefficientInput(
            crop_name="CropB",
            crop_type="TypeB",
            kc_initial=0.4,
            kc_mid_season=0.8,
            kc_final=1.2,
            active=True,
        )
        crop_coefficient_2 = CropCoefficientInput(
            crop_name="CropC",
            crop_type="TypeC",
            kc_initial=0.7,
            kc_mid_season=1.2,
            kc_final=1.8,
            active=True,
        )
        self.service.upsert(crop_coefficient_1)
        self.service.upsert(crop_coefficient_2)

        # Verifica se ttodos os coeficientes foram obtidos ccorretamente
        all_coefficients = self.service.get_all(test_db)
        assert len(all_coefficients) == 2
        assert all_coefficients[0].crop_name == "CropB"
        assert all_coefficients[1].crop_name == "CropC"

    def test_get_id(self, test_db):
        # Teste para obter um coeficiente de cultivo por ID
        crop_coefficient = CropCoefficientInput(
            crop_name="CropD",
            crop_type="TypeD",
            kc_initial=0.6,
            kc_mid_season=1.0,
            kc_final=1.5,
            active=True,
        )
        self.service.upsert(crop_coefficient)

        # Obtém o ID
        retrieved_id = self.repo.get_all(test_db)[0].id

        # Verifica se o coeficiente foi obtido corretamente pelo ID
        retrieved = self.service.get_id(test_db, retrieved_id)
        assert retrieved.crop_name == "CropD"

    # Teste para atualização condicional
    def test_upsert_conditional(self, test_db):
        # Adicionar um coeficiente inicial
        initial_coefficient = CropCoefficientInput(
            crop_name="InitialCrop",
            crop_type="InitialType",
            kc_initial=0.5,
            kc_mid_season=1.0,
            kc_final=1.5,
            active=True,
        )
        self.service.upsert(initial_coefficient)

        # Atualizar o coeficiente inicial
        updated_coefficient = CropCoefficientInput(
            crop_name="UpdatedCrop",
            crop_type="UpdatedType",
            kc_initial=0.8,
            kc_mid_season=1.2,
            kc_final=1.7,
            active=True,
        )
        self.service.upsert(updated_coefficient)

        # Verifcar se o coeficiente inicial foi atualizado corretamente
        all_coefficients = self.service.get_all(test_db)
        assert len(all_coefficients) == 1
        assert all_coefficients[0].crop_name == "UpdatedCrop"

    # Testes de falha
    def test_get_invalid_id(self, test_db):
        # Tentar obter um coeficiente com um ID inválido
        with pytest.raises(AttributeError):
            self.service.get_id(test_db, "invalid_id")

    def test_invalid_data(self, test_db):
        # Testar inserção com campos obrigatórios ausentes
        invalid_coefficient = CropCoefficientInput(
            kc_initial=0.5, kc_mid_season=1.0, kc_final=1.5, active=True
        )
        with pytest.raises(Exception):
            self.service.upsert(invalid_coefficient)

    # Testes de cenários
    def test_empty_database(self, test_db):
        # Testar obter todos os coeficientes vom o banco de dados está vazio
        all_coefficients = self.service.get_all(test_db)
        assert len(all_coefficients) == 0

    def test_existing_data(self, test_db):
        # Testar operações em um banco de dados com dados pré-existentes
        initial_coefficient = CropCoefficientInput(
            crop_name="InitialCrop",
            crop_type="InitialType",
            kc_initial=0.5,
            kc_mid_season=1.0,
            kc_final=1.5,
            active=True,
        )
        self.service.upsert(initial_coefficient)

        # Verificar se o coeficiente foi inseido corretament
        all_coefficients = self.service.get_all(test_db)
        assert len(all_coefficients) == 1
