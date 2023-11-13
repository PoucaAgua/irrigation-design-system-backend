import pytest

from core.domain.entity.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.mappers.crop_coefficient import CropCoefficientMapper
from infrastructure.persistence.models import CropCoefficientModel


class TestCropCoefficientMapper:

    @staticmethod
    def __assert_that_models(result: CropCoefficientModel, expected: CropCoefficientModel):
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
                        kc_initial=0.5,
                        kc_mid_season=1,
                        kc_final=2,
                        active=True
                    ),
                    CropCoefficientModel(
                        id=1,
                        crop_name="crop_name",
                        crop_type="crop_type",
                        kc_initial=0.5,
                        kc_mid_season=1,
                        kc_final=2,
                        active=True
                    )
            ),
        ],
    )
    def test_entity_to_model(self, input: CropCoefficientInput, expected_result: CropCoefficientModel):
        result = CropCoefficientMapper.entity_to_model(input)
        self.__assert_that_models(result, expected_result)
