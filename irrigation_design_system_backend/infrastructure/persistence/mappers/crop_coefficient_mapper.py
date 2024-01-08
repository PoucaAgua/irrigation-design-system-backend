from core.domain.entity.crop_coefficient_input import CropCoefficientInput

from infrastructure.persistence.models.crop_coefficient_model import CropCoefficientModel


class CropCoefficientMapper:
    @staticmethod
    def model_from_input(crop_coefficient_input: CropCoefficientInput) -> CropCoefficientModel:
        field_mappings = {
            "crop_id": crop_coefficient_input.crop_id,
            "crop_name": crop_coefficient_input.crop_name,
            "crop_type": crop_coefficient_input.crop_type,
            "kc_initial": crop_coefficient_input.kc_initial,
            "kc_mid_season": crop_coefficient_input.kc_mid_season,
            "kc_final": crop_coefficient_input.kc_final,
            "is_active": crop_coefficient_input.is_active,
        }
        return CropCoefficientModel(**field_mappings)

    @staticmethod
    def model_from_input_and_persisted(
        crop_coefficient_input: CropCoefficientInput,
        persisted_crop_coefficient: CropCoefficientModel,
    ) -> CropCoefficientModel:
        field_mappings = {
            "crop_id": crop_coefficient_input.crop_id,
            "crop_name": crop_coefficient_input.crop_name or persisted_crop_coefficient.crop_name,
            "crop_type": crop_coefficient_input.crop_type or persisted_crop_coefficient.crop_type,
            "kc_initial": (
                crop_coefficient_input.kc_initial or persisted_crop_coefficient.kc_initial
            ),
            "kc_mid_season": (
                crop_coefficient_input.kc_mid_season or persisted_crop_coefficient.kc_mid_season
            ),
            "kc_final": (crop_coefficient_input.kc_final or persisted_crop_coefficient.kc_final),
            "is_active": crop_coefficient_input.is_active or persisted_crop_coefficient.is_active,
        }
        return CropCoefficientModel(**field_mappings)
