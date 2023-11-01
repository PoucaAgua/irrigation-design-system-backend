from infrastructure.persistence.models.crop_coefficient import CropCoefficientModel
from core.domain.entity.crop_coefficient_entity import CropCoefficientEntity


class CropCoefficientMapper:
    @staticmethod
    def entity_to_model(crop_coefficient_entity: CropCoefficientEntity) -> CropCoefficientModel:
        return CropCoefficientModel(
            crop_name=crop_coefficient_entity.crop_name,
            crop_type=crop_coefficient_entity.crop_type,
            kc_initial=crop_coefficient_entity.kc_initial,
            kc_mid_season=crop_coefficient_entity.kc_mid_season,
            kc_final=crop_coefficient_entity.kc_final,
        )

    @staticmethod
    def model_to_entity(crop_coefficient_model: CropCoefficientModel) -> CropCoefficientEntity:
        return CropCoefficientEntity(
            crop_name=crop_coefficient_model.crop_name,
            crop_type=crop_coefficient_model.crop_type,
            kc_initial=crop_coefficient_model.kc_initial,
            kc_mid_season=crop_coefficient_model.kc_mid_season,
            kc_final=crop_coefficient_model.kc_final,
        )
