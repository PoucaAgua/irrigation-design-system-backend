import pytest
from decimal import Decimal
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.mappers.crop_coefficient import CropCoefficientMapper
from infrastructure.persistence.models.crop_coefficient import CropCoefficientModel


class TestCropCoefficientMapper:

    def assert_that_models(self, result: CropCoefficientModel, expected: CropCoefficientModel):
        assert isinstance(result, CropCoefficientModel)
        assert result.id == expected.id, "ID mismatch"
        assert result.crop_type == expected.crop_type, "Crop type mismatch"
        assert result.kc_initial == expected.kc_initial, "kc_initial mismatch"
        assert result.kc_mid_season == expected.kc_mid_season, "kc_mid_season mismatch"
        assert result.kc_final == expected.kc_final, "kc_final mismatch"
        assert result.active == expected.active, "Active mismatch"

    @pytest.mark.parametrize(
        "input, expected_result",
        [
            (
                CropCoefficientInput(
                    id=1,
                    crop_name="crop_name",
                    crop_type="crop_type",
                    kc_initial=Decimal("0.5"),
                    kc_mid_season=Decimal("1"),
                    kc_final=Decimal("2"),
                    active=True,
                ),
                CropCoefficientModel(
                    id=1,
                    crop_name="crop_name",
                    crop_type="crop_type",
                    kc_initial=0.5,
                    kc_mid_season=1,
                    kc_final=2,
                    active=True,
                ),
            ),
            (
                CropCoefficientInput(
                    id=2,
                    crop_name="corn",
                    crop_type="type",
                    kc_initial=None,
                    kc_mid_season=None,
                    kc_final=None,
                    active=False,
                ),
                CropCoefficientModel(
                    id=2,
                    crop_name="corn",
                    crop_type="type",
                    kc_initial=None,
                    kc_mid_season=None,
                    kc_final=None,
                    active=False,
                ),
            ),
            (
                CropCoefficientInput(
                    id=3,
                    crop_name="wheat",
                    crop_type="type",
                    kc_initial=None,
                    kc_mid_season=None,
                    kc_final=None,
                    active=False,
                ),
                CropCoefficientModel(
                    id=3,
                    crop_name="wheat",
                    crop_type="type",
                    kc_initial=Decimal("0.3"),
                    kc_mid_season=Decimal("0.6"),
                    kc_final=Decimal("0.9"),
                    active=True,
                ),
            ),
        ],
    )
    def test_entity_to_model(
        self, input: CropCoefficientInput, expected_result: CropCoefficientModel
    ):
        result = CropCoefficientMapper.entity_to_model(input)
        self.assert_that_models(result, expected_result)

    def test_entity_to_model_persisted(self):
        entity_input = CropCoefficientInput(
            id=1,
            crop_name="corn",
            crop_type="type",
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=False,
        )
        persisted_model = CropCoefficientModel(
            id=1,
            crop_name="persisted_corn",
            crop_type="persisted_type",
            kc_initial=0.3,
            kc_mid_season=0.6,
            kc_final=0.9,
            active=True,
        )

        result = CropCoefficientMapper.entity_to_model_persisted(entity_input, persisted_model)

        assert result.id == 1, "ID mismatch"
        assert result.crop_name == "corn", "Crop name mismatch"
        assert result.crop_type == "type", "Crop type mismatch"
        assert result.kc_initial == 0.3, "kc_initial mismatch"
        assert result.kc_mid_season == 0.6, "kc_mid_season mismatch"
        assert result.kc_final == 0.9, "kc_final mismatch"
        assert result.active is False, "Active mismatch"

    def test_model_to_entity(self):
        model = CropCoefficientModel(
            id=4,
            crop_name="new_crop",
            crop_type="new_type",
            kc_initial=Decimal('0.7'),
            kc_mid_season=Decimal('1.1'),
            kc_final=Decimal('1.5'),
            active=True,
        )

        result = CropCoefficientMapper.model_to_entity(model)

        assert result.crop_name == "new_crop", "Crop name mismatch"
        assert result.crop_type == "new_type", "Crop type mismatch"
        assert result.kc_initial == Decimal('0.7'), "kc_initial mismatch"
        assert result.kc_mid_season == Decimal('1.1'), "kc_mid_season mismatch"
        assert result.kc_final == Decimal('1.5'), "kc_final mismatch"

