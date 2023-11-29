import pytest
from decimal import Decimal
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.mappers.crop_coefficient import CropCoefficientMapper
from infrastructure.persistence.models.crop_coefficient import CropCoefficientModel


class TestCropCoefficientMapper:

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
                    kc_initial=Decimal("0.3"),
                    kc_mid_season=Decimal("0.6"),
                    kc_final=Decimal("0.9"),
                    active=True,
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
        assert result == expected_result

    def test_entity_to_model_persisted(self):
        # given
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
            kc_initial=Decimal("0.3"),
            kc_mid_season=Decimal("0.6"),
            kc_final=Decimal("0.9"),
            active=True,
        )

        expected_result = CropCoefficientModel(
            id=1,
            crop_name="corn",
            crop_type="type",
            kc_initial=Decimal("0.3"),
            kc_mid_season=Decimal("0.6"),
            kc_final=Decimal("0.9"),
            active=False,
        )

        # when
        result = CropCoefficientMapper.entity_to_model_persisted(entity_input, persisted_model)

        assert result == expected_result

    def test_entity_to_model_additional(self):
        input_data = CropCoefficientInput(
            id=4,
            crop_name="rice",
            crop_type="long grain",
            kc_initial=Decimal("0.6"),
            kc_mid_season=Decimal("1.2"),
            kc_final=Decimal("1.8"),
            active=True,
        )
        expected_result = CropCoefficientModel(
            id=4,
            crop_name="rice",
            crop_type="long grain",
            kc_initial=0.6,
            kc_mid_season=1.2,
            kc_final=1.8,
            active=True,
        )
        result = CropCoefficientMapper.entity_to_model(input_data)

        assert result == expected_result

    def test_entity_to_model_persisted_additional(self):
        # Given
        entity_input = CropCoefficientInput(
            id=5,
            crop_name="potato",
            crop_type="white",
            kc_initial=Decimal("0.4"),
            kc_mid_season=Decimal("0.8"),
            kc_final=Decimal("1.4"),
            active=True,
        )
        persisted_model = CropCoefficientModel(
            id=5,
            crop_name="persisted_potato",
            crop_type="persisted_white",
            kc_initial=0.5,
            kc_mid_season=0.9,
            kc_final=1.5,
            active=True,
        )
        expected_result = CropCoefficientModel(
            id=5,
            crop_name="potato",
            crop_type="white",
            kc_initial=0.4,
            kc_mid_season=0.8,
            kc_final=1.4,
            active=True,
        )

        # When
        result = CropCoefficientMapper.entity_to_model_persisted(entity_input, persisted_model)

        # Assert
        assert result == expected_result
