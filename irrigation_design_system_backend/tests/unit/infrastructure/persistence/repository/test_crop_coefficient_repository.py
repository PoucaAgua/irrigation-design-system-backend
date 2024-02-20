import pytest
from unittest.mock import Mock, patch
from infrastructure.persistence.repository.crop_coefficient_repository import (
    CropCoefficientRepository,
)
from infrastructure.persistence.models.crop_coefficient_model import CropCoefficientModel
from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput


class TestCropCoefficientRepository:
    repository = CropCoefficientRepository()

    @pytest.fixture
    def db(self):
        return Mock()

    @patch(
        "infrastructure.persistence.repository.crop_coefficient_repository.CropCoefficientMapper"
    )
    def test_upsert_insert(self, crop_coefficient_mapper_mock, db):
        # given
        crop_coefficient_input = CropCoefficientInput(
            crop_id=1,
            crop_name="Test Crop",
            crop_type="Test Type",
            kc_initial=1.5,
            kc_mid_season=2.0,
            kc_final=1.8,
            is_active=True,
        )

        crop_coefficient_db_mock = CropCoefficientModel(crop_id=None)
        crop_coefficient_mapper_mock.entity_to_model.return_value = crop_coefficient_db_mock

        # when
        result = self.repository.upsert(db=db, crop_coefficient=crop_coefficient_input)

        # then
        assert crop_coefficient_db_mock == result
        crop_coefficient_mapper_mock.entity_to_model.assert_called_with(crop_coefficient_input)
        db.add.assert_called_with(crop_coefficient_db_mock)
        db.commit.assert_called_once()
        db.close.assert_called_once()

    @patch(
        "infrastructure.persistence.repository.crop_coefficient_repository.CropCoefficientMapper"
    )
    def test_upsert_update(self, crop_coefficient_mapper_mock, db):
        # given
        crop_coefficient_input = Mock()
        crop_coefficient_db_mock = Mock(crop_id=1)
        crop_coefficient_db_persisted_mock = Mock(crop_id=1)
        crop_coefficient_db_mock_2 = Mock(crop_id=1)

        crop_coefficient_mapper_mock.entity_to_model.return_value = crop_coefficient_db_mock
        db.query().filter().first.return_value = crop_coefficient_db_persisted_mock

