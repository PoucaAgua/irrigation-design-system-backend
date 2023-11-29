import pytest
from unittest.mock import MagicMock
from decimal import Decimal
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from irrigation_design_system_backend.apps.crop_coefficient.crop_coefficient import (
    CropCoefficientService,
)


class TestCropCoefficientService:
    def test_upsert(self):
        mock_repo = MagicMock()
        service = CropCoefficientService(repository=mock_repo)

        crop_coefficient = CropCoefficientInput(
            crop_name="CropA",
            crop_type="TypeA",
            kc_initial=Decimal("0.5"),
            kc_mid_season=Decimal("1.0"),
            kc_final=Decimal("1.5"),
            active=True,
        )

        service.upsert(crop_coefficient)

        mock_repo.upsert.assert_called_once_with(crop_coefficient)

        crop_coefficient.id = 1
        crop_coefficient.crop_name = "UpdatedCropA"

        service.upsert(crop_coefficient)

        mock_repo.upsert.assert_called_with(crop_coefficient)

    def test_delete(self):
        mock_repo = MagicMock()
        service = CropCoefficientService(repository=mock_repo)

        existing_coefficient = CropCoefficientInput(
            id=1,
            crop_name="ExistingCrop",
            crop_type="ExistingType",
            kc_initial=Decimal("0.5"),
            kc_mid_season=Decimal("1.0"),
            kc_final=Decimal("1.5"),
            active=True,
        )

        service.delete(existing_coefficient.id)

        mock_repo.delete.assert_called_once_with(existing_coefficient.id)

    def test_get_id(self):
        mock_repo = MagicMock()
        service = CropCoefficientService(repository=mock_repo)

        target_id = 1
        expected_coefficient = CropCoefficientInput(
            id=target_id,
            crop_name="TestCrop",
            crop_type="TestType",
            kc_initial=Decimal("0.6"),
            kc_mid_season=Decimal("1.2"),
            kc_final=Decimal("1.8"),
            active=True,
        )

        mock_repo.get_id.return_value = expected_coefficient

        retrieved_coefficient = service.get_id(mock_repo, target_id)

        assert retrieved_coefficient == expected_coefficient

    def test_get_all(self):
        mock_repo = MagicMock()
        service = CropCoefficientService(repository=mock_repo)

        all_coefficients = [
            CropCoefficientInput(
                id=1,
                crop_name="CropA",
                crop_type="TypeA",
                kc_initial=Decimal("0.5"),
                kc_mid_season=Decimal("1.0"),
                kc_final=Decimal("1.5"),
                active=True,
            ),
            CropCoefficientInput(
                id=2,
                crop_name="CropB",
                crop_type="TypeB",
                kc_initial=Decimal("0.7"),
                kc_mid_season=Decimal("1.1"),
                kc_final=Decimal("1.6"),
                active=True,
            ),
        ]

        mock_repo.get_all.return_value = all_coefficients

        retrieved_coefficients = service.get_all(mock_repo)

        assert retrieved_coefficients == all_coefficients

    def test_empty_database(self):
        mock_repo = MagicMock()
        service = CropCoefficientService(repository=mock_repo)

        mock_repo.get_all.return_value = []

        retrieved_coefficients = service.get_all(mock_repo)

        assert retrieved_coefficients == []

    def test_invalid_id_update(self):
        mock_repo = MagicMock()
        service = CropCoefficientService(repository=mock_repo)

        invalid_coefficient = CropCoefficientInput(
            id=100,
            crop_name="InvalidCrop",
            crop_type="InvalidType",
            kc_initial=Decimal("0.3"),
            kc_mid_season=Decimal("0.6"),
            kc_final=Decimal("0.9"),
            active=True,
        )

        with pytest.raises(ValueError):
            service.upsert(invalid_coefficient)

    def test_invalid_data_insert(self):
        mock_repo = MagicMock()
        service = CropCoefficientService(repository=mock_repo)

        invalid_coefficient = CropCoefficientInput(
            kc_initial=Decimal("0.5"),
            kc_mid_season=Decimal("1.0"),
            kc_final=Decimal("1.5"),
            active=True,
        )

        with pytest.raises(ValueError):
            service.upsert(invalid_coefficient)

    def test_invalid_id_get(self):
        mock_repo = MagicMock()
        service = CropCoefficientService(repository=mock_repo)

        invalid_id = "invalid_id"

        with pytest.raises(ValueError):
            service.get_id(mock_repo, invalid_id)
