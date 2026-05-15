from decimal import Decimal
from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput
from core.domain.entity.crop_coefficient.crop_coefficient_output import CropCoefficientResponse
from infrastructure.persistence.mappers.crop_coefficient_mapper import CropCoefficientMapper
from infrastructure.persistence.models.crop_coefficient_model import CropCoefficientModel


class TestCropCoefficientMapper:
    def test_entity_to_model(self):
        # Arrange
        input_entity = CropCoefficientInput(
            crop_id=1,
            crop_name="Test Crop",
            crop_type="Test Type",
            kc_initial=Decimal("1.5"),
            kc_mid_season=Decimal("2.0"),
            kc_final=Decimal("1.8"),
            is_active=True,
        )

        # Act
        result_model = CropCoefficientMapper.entity_to_model(input_entity)

        # Assert
        assert isinstance(result_model, CropCoefficientModel)
        assert result_model.crop_id == 1
        assert result_model.crop_name == "Test Crop"
        assert result_model.crop_type == "Test Type"
        assert result_model.kc_initial == 1.5
        assert result_model.kc_mid_season == 2.0
        assert result_model.kc_final == Decimal("1.8")
        assert result_model.is_active is True

    def test_update_model_from_entity(self):
        # Arrange
        input_model = CropCoefficientModel(
            crop_id=1,
            crop_name="Test Crop",
            crop_type="Test Type",
            kc_initial=1.5,
            kc_mid_season=2.0,
            kc_final=1.8,
            is_active=True,
        )

        input_entity = CropCoefficientInput(
            crop_id=None,
            crop_name="Updated Crop",
            crop_type="Updated Type",
            kc_initial=Decimal("1.7"),
            kc_mid_season=None,
            kc_final=None,
            is_active=False,
        )

        # Act
        CropCoefficientMapper.update_model_from_entity(input_model, input_entity)

        # Assert
        assert input_model.crop_id == 1
        assert input_model.crop_name == "Updated Crop"
        assert input_model.crop_type == "Updated Type"
        assert input_model.kc_initial == Decimal("1.7")
        assert input_model.kc_mid_season == 2.0
        assert input_model.kc_final == 1.8
        assert input_model.is_active is False

    def test_entity_to_model_persisted(self):
        # Arrange
        input_entity = CropCoefficientInput(
            crop_id=1,
            crop_name="crop",
            crop_type="type",
            kc_initial=Decimal("2.0"),
            kc_mid_season=Decimal("2.5"),
            kc_final=Decimal("2.2"),
            is_active=True,
        )

        persisted_model = CropCoefficientModel(
            crop_id=1,
            crop_name="crop",
            crop_type="type",
            kc_initial=Decimal("2.0"),
            kc_mid_season=Decimal("2.5"),
            kc_final=Decimal("2.2"),
            is_active=True,
        )

        # Act
        result_model = CropCoefficientMapper.entity_to_model_persisted(
            input_entity, persisted_model
        )

        # Assert
        assert isinstance(result_model, CropCoefficientModel)
        assert result_model.crop_id == 1
        assert result_model.crop_name == "crop"
        assert result_model.crop_type == "type"
        assert result_model.kc_initial == Decimal("2.0")
        assert result_model.kc_mid_season == Decimal("2.5")
        assert result_model.kc_final == Decimal("2.2")
        assert result_model.is_active is True

    def test_to_response(self):
        # Arrange
        input_model = CropCoefficientModel(
            crop_id=1,
            crop_name="Test Crop",
            crop_type="Test Type",
            kc_initial=1.5,
            kc_mid_season=2.0,
            kc_final=Decimal("1.8"),
            is_active=True,
        )

        # Act
        result_response = CropCoefficientMapper.to_response(input_model)

        # Assert
        assert isinstance(result_response, CropCoefficientResponse)
        assert result_response.crop_id == 1
        assert result_response.crop_name == "Test Crop"
        assert result_response.crop_type == "Test Type"
        assert result_response.kc_initial == Decimal("1.5")
        assert result_response.kc_mid_season == Decimal("2.0")
        assert result_response.kc_final == Decimal("1.8")
        assert result_response.is_active is True

    def test_entity_to_model_with_none_values(self):
        # Arrange
        input_entity = CropCoefficientInput(
            crop_id=None,
            crop_name=None,
            crop_type=None,
            kc_initial=None,
            kc_mid_season=None,
            kc_final=None,
            is_active=False,
        )

        # Act
        result_model = CropCoefficientMapper.entity_to_model(input_entity)

        # Assert
        assert isinstance(result_model, CropCoefficientModel)
        assert result_model.crop_id is None
        assert result_model.crop_name is None
        assert result_model.crop_type is None
        assert result_model.kc_initial is None
        assert result_model.kc_mid_season is None
        assert result_model.kc_final is None
        assert result_model.is_active is False
