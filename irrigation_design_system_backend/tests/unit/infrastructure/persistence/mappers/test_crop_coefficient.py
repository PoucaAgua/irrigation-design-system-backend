from decimal import Decimal
from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.mappers.crop_coefficient import CropCoefficientMapper
from infrastructure.persistence.models.crop_coefficient import CropCoefficientModel


class TestCropCoefficientMapper:
    def test_model_from_input(self):
        # Given
        input_data = CropCoefficientInput(
            id=1,
            crop_name="crop_name",
            crop_type="crop_type",
            kc_initial=Decimal("0.5"),
            kc_mid_season=Decimal("1"),
            kc_final=Decimal("2"),
            active=True,
        )

        expected_output = CropCoefficientModel(
            id=1,
            crop_name="crop_name",
            crop_type="crop_type",
            kc_initial=0.5,
            kc_mid_season=1,
            kc_final=2,
            active=True,
        )

        # When
        result = CropCoefficientMapper.entity_to_model(input_data)

        assert isinstance(result, CropCoefficientModel)
        assert result.id == expected_output.id
        assert result.crop_name == expected_output.crop_name
        assert result.crop_type == expected_output.crop_type
        assert result.kc_initial == expected_output.kc_initial
        assert result.kc_mid_season == expected_output.kc_mid_season
        assert result.kc_final == expected_output.kc_final
        assert result.active == expected_output.active

    def test_entity_to_model_and_persisted(self):
        # Given
        input_data = CropCoefficientInput(
            id=1,
            crop_name="crop_name",
            crop_type="crop_type",
            kc_initial=Decimal("0.5"),
            kc_mid_season=Decimal("1"),
            kc_final=Decimal("2"),
            active=True,
        )

        persisted_model = CropCoefficientModel(
            id=1,
            crop_name="crop_name",
            crop_type="crop_type",
            kc_initial=Decimal("0.5"),
            kc_mid_season=Decimal("1"),
            kc_final=Decimal("2"),
            active=True,
        )

        expected_output = CropCoefficientModel(
            id=1,
            crop_name="crop_name",
            crop_type="crop_type",
            kc_initial=0.5,
            kc_mid_season=1,
            kc_final=2,
            active=True,
        )

        # When
        result = CropCoefficientMapper.entity_to_model_persisted(input_data, persisted_model)

        assert isinstance(result, CropCoefficientModel)
        assert result.id == expected_output.id
        assert result.crop_name == expected_output.crop_name
        assert result.crop_type == expected_output.crop_type
        assert result.kc_initial == expected_output.kc_initial
        assert result.kc_mid_season == expected_output.kc_mid_season
        assert result.kc_final == expected_output.kc_final
        assert result.active == expected_output.active

    def test_entity_to_model_persisted_multiple(self):
        # Given
        crop_coefficient_input = CropCoefficientInput(
            id=1,
            crop_name="crop_name",
            crop_type="crop_type",
            kc_initial=Decimal("0.5"),
            kc_mid_season=Decimal("1"),
            kc_final=Decimal("2"),
            active=True,
        )

        persisted_models = [
            CropCoefficientModel(
                id=1,
                crop_name="crop_name",
                crop_type="crop_type",
                kc_initial=0.5,
                kc_mid_season=1,
                kc_final=2,
                active=True,
            ),
            CropCoefficientModel(
                id=1,
                crop_name="crop_name",
                crop_type="crop_type",
                kc_initial=0.5,
                kc_mid_season=1,
                kc_final=2,
                active=False,
            ),
        ]

        # When
        expected_output = CropCoefficientModel(
            id=1,
            crop_name="crop_name",
            crop_type="crop_type",
            kc_initial=0.5,
            kc_mid_season=1,
            kc_final=2,
            active=True,
        )

        result = CropCoefficientMapper.entity_to_model_persisted(
            crop_coefficient_input, persisted_models
        )

        assert isinstance(result, CropCoefficientModel)
        assert result.id == expected_output.id
        assert result.crop_name == expected_output.crop_name
        assert result.crop_type == expected_output.crop_type
        assert result.kc_initial == expected_output.kc_initial
        assert result.kc_mid_season == expected_output.kc_mid_season
        assert result.kc_final == expected_output.kc_final
        assert result.active == expected_output.active

    def test_invalid_input(self):
        # Given
        crop_input = CropCoefficientInput(
            id=None,
            crop_name="",
            crop_type="",
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=False,
        )

        # When
        result = CropCoefficientMapper.entity_to_model(crop_input)

        # Check if result fields are None or empty
        assert (
            result.id is None
            and result.crop_name == ""
            and result.crop_type == ""
            and result.kc_initial is None
            and result.kc_mid_season is None
            and result.kc_final is None
            and result.active is False
        )

    def test_entity_to_model_empty_input(self):
        # Given
        empty_crop_input = CropCoefficientInput()

        # When
        result = CropCoefficientMapper.entity_to_model(empty_crop_input)

        # Assert if result is None
        assert result is None or (
            result.id is None
            and result.crop_name is None
            and result.crop_type is None
            and result.kc_initial is None
            and result.kc_mid_season is None
            and result.kc_final is None
            and result.active is True
        )

    def test_entity_to_model_non_negative_values(self):
        # Given
        non_negative_input = CropCoefficientInput(
            id=10,
            crop_name="test_crop",
            crop_type="test_type",
            kc_initial=Decimal("0.5"),
            kc_mid_season=Decimal("1"),
            kc_final=Decimal("2"),
            active=True,
        )

        expected_output = CropCoefficientModel(
            id=10,
            crop_name="test_crop",
            crop_type="test_type",
            kc_initial=0.5,
            kc_mid_season=1,
            kc_final=2,
            active=True,
        )

        # When
        result = CropCoefficientMapper.entity_to_model(non_negative_input)

        assert result == expected_output

    def test_entity_to_model_null_values_v2(self):
        # Given
        null_values_input = CropCoefficientInput(
            id=15,
            crop_name="null_test_crop",
            crop_type="null_test_type",
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=True,
        )

        expected_output = CropCoefficientModel(
            id=15,
            crop_name="null_test_crop",
            crop_type="null_test_type",
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=True,
        )

        # When
        result = CropCoefficientMapper.entity_to_model(null_values_input)

        # Check if the entire 'result' object matches 'expected_output' object
        assert result == expected_output

    def test_entity_to_model_all_zeros(self):
        # input_data
        all_zeros_input = CropCoefficientInput(
            id=20,
            crop_name="zero_crop",
            crop_type="zero_type",
            kc_initial=Decimal("0"),
            kc_mid_season=Decimal("0"),
            kc_final=Decimal("0"),
            active=True,
        )

        # expected_output
        expected_output = CropCoefficientModel(
            id=20,
            crop_name="zero_crop",
            crop_type="zero_type",
            kc_initial=0,
            kc_mid_season=0,
            kc_final=0,
            active=True,
        )

        result = CropCoefficientMapper.entity_to_model(all_zeros_input)

        # Check each field individually for '0'
        assert result.id == expected_output.id
        assert result.crop_name == expected_output.crop_name
        assert result.crop_type == expected_output.crop_type
        assert result.kc_initial == expected_output.kc_initial
        assert result.kc_mid_season == expected_output.kc_mid_season
        assert result.kc_final == expected_output.kc_final
        assert result.active == expected_output.active

    def test_entity_to_model_high_values(self):
        # Given
        high_values_input = CropCoefficientInput(
            id=30,
            crop_name="high_crop",
            crop_type="high_type",
            kc_initial=Decimal("1000"),
            kc_mid_season=Decimal("5000"),
            kc_final=Decimal("10000"),
            active=True,
        )

        expected_output = CropCoefficientModel(
            id=30,
            crop_name="high_crop",
            crop_type="high_type",
            kc_initial=1000,
            kc_mid_season=5000,
            kc_final=10000,
            active=True,
        )

        # When
        result = CropCoefficientMapper.entity_to_model(high_values_input)

        assert result == expected_output

    def test_entity_to_model_no_values(self):
        # Given
        no_values_input = CropCoefficientInput(
            id=None,
            crop_name=None,
            crop_type=None,
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=True,
        )

        expected_output = CropCoefficientModel(
            id=None,
            crop_name=None,
            crop_type=None,
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=True,
        )

        # When
        result = CropCoefficientMapper.entity_to_model(no_values_input)

        assert result == expected_output

    def test_entity_to_model_null_value(self):
        # Given
        null_input = CropCoefficientInput(
            id=None,
            crop_name="Sunflower",
            crop_type=None,
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=False,
        )

        expected_output = CropCoefficientModel(
            id=None,
            crop_name="Sunflower",
            crop_type=None,
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=False,
        )

        # When
        result = CropCoefficientMapper.entity_to_model(null_input)

        assert result == expected_output

    def test_entity_to_model_null_values(self):
        # Given
        null_input = CropCoefficientInput(
            id=6,
            crop_name="Carrot",
            crop_type="Orange",
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=False,
        )

        expected_output = CropCoefficientModel(
            id=6,
            crop_name="Carrot",
            crop_type="Orange",
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            active=False,
        )

        # When
        result = CropCoefficientMapper.entity_to_model(null_input)

        assert result == expected_output
