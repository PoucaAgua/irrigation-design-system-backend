import pytest
from unittest.mock import Mock, patch
from infrastructure.persistence.repository.crop_coefficient_repository import CropCoefficientRepository


class TestCropCoefficientRepository:

    repository = CropCoefficientRepository()

    @pytest.fixture
    def db(self):
        return Mock()

    @patch('infrastructure.persistence.repository.crop_coefficient_repository.CropCoefficientMapper')
    def test_upsert_insert(self, crop_coefficient_mapper_mock, db):
        # given
        coefficient_input = Mock()
        coefficient_db_mock = Mock(id=None)
        crop_coefficient_mapper_mock.entity_to_model.return_value = coefficient_db_mock

        # when
        result = self.repository.upsert(db=db, crop_coefficient=coefficient_input)

        # then
        assert coefficient_db_mock == result
        crop_coefficient_mapper_mock.entity_to_model.assert_called_with(coefficient_input)
        db.add.assert_called_with(coefficient_db_mock)
        db.commit.assert_called_once()
        db.close.assert_called_once()

    @patch('infrastructure.persistence.repository.crop_coefficient_repository.CropCoefficientMapper')
    def test_upsert_update(self, crop_coefficient_mapper_mock, db):
        # given
        coefficient_input = Mock()
        coefficient_db_mock = Mock(id=1)
        coefficient_db_persisted_mock = Mock(id=1)
        coefficient_db_mock_2 = Mock(id=1)

        crop_coefficient_mapper_mock.entity_to_model.return_value = coefficient_db_mock
        db.query().filter().first.return_value = coefficient_db_persisted_mock
        crop_coefficient_mapper_mock.entity_to_model_persisted.return_value = coefficient_db_mock_2

        # when
        result = self.repository.upsert(db=db, crop_coefficient=coefficient_input)

        # then
        crop_coefficient_mapper_mock.entity_to_model.assert_called_once_with(coefficient_input)
        crop_coefficient_mapper_mock.entity_to_model_persisted.assert_called_once_with(
            coefficient_input, coefficient_db_persisted_mock
        )

        db.merge.assert_called_with(coefficient_db_mock_2)
        db.commit.assert_called_once()
        db.close.assert_called_once()
