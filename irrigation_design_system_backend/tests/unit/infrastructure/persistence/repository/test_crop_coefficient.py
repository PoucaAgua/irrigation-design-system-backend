import pytest
from unittest.mock import Mock, patch
from infrastructure.persistence.repository.crop_coefficient_repository import CropCoefficientRepository

class CropCoefficientNotFoundError(Exception):
    pass

try:
    class TestCropCoefficientRepository:

        repository = CropCoefficientRepository()

        @pytest.fixture
        def db(self):
            return Mock()

        @patch('infrastructure.persistence.repository.crop_coefficient_repository.CropCoefficientMapper')
        def test_upsert_insert(self, crop_coefficient_mapper_mock, db):
            # given
            coefficient_input = Mock(id=None)
            coefficient_db_mock = Mock()
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
            coefficient_input = Mock(id=1)
            coefficient_db_mock = Mock()
            coefficient_db_persisted_mock = Mock(id=1)
            coefficient_db_mock_2 = Mock(id=1)

            crop_coefficient_mapper_mock.entity_to_model.return_value = coefficient_db_mock
            db.query().filter().first.return_value = coefficient_db_persisted_mock
            crop_coefficient_mapper_mock.entity_to_model_persisted.return_value = coefficient_db_mock_2

            # when
            result = self.repository.upsert(db=db, crop_coefficient=coefficient_input)

            # then
            assert coefficient_db_mock_2 == result
            crop_coefficient_mapper_mock.entity_to_model_persisted.assert_called_once_with(
                coefficient_input, coefficient_db_persisted_mock
            )

            db.merge.assert_called_with(coefficient_db_mock_2)
            db.commit.assert_called_once()
            db.close.assert_called_once()

        def test_upsert_invalid_id(self, db):
            # given
            coefficient_input = Mock(id=1)
            db.query().filter().first.return_value = None

            # when & then
            with pytest.raises(FileNotFoundError) as exc_info:
                self.repository.upsert(db=db, crop_coefficient=coefficient_input)

            assert str(exc_info.value) == "invalid id 1"
            db.merge.assert_not_called()
            db.commit.assert_not_called()
            db.close.assert_called_once()

except CropCoefficientNotFoundError as e:
    print(f"Error: {e}")


