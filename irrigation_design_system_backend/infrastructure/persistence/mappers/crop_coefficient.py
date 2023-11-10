from infrastructure.persistence.models.crop_coefficient import CropCoefficientModel
from core.domain.entity.crop_coefficient_input import CropCoefficientInput


class CropCoefficientMapper:
    @staticmethod
    def entity_to_model(crop_coefficient_input: CropCoefficientInput) -> CropCoefficientModel:
        return CropCoefficientModel(
            id=crop_coefficient_input.id,
            crop_name=crop_coefficient_input.crop_name,
            crop_type=crop_coefficient_input.crop_type,
            kc_initial=crop_coefficient_input.kc_initial,
            kc_mid_season=crop_coefficient_input.kc_mid_season,
            kc_final=crop_coefficient_input.kc_final,
            active=crop_coefficient_input.active,
        )

    @staticmethod
    def entity_to_model_persisted(
        entity_input: CropCoefficientInput, persisted: CropCoefficientModel
    ):
        field_mappings = dict(
            id=entity_input.id,
            crop_name=entity_input.crop_name or persisted.crop_name,
            crop_type=entity_input.crop_type or persisted.crop_type,
            kc_initial=entity_input.kc_initial or persisted.kc_initial,
            kc_mid_season=entity_input.kc_mid_season or persisted.kc_mid_season,
            kc_final=entity_input.kc_final or persisted.kc_final,
            active=persisted.active if entity_input.active is None else entity_input.active,
        )
        return CropCoefficientModel(**field_mappings)

    @staticmethod
    def model_to_entity(crop_coefficient_model: CropCoefficientModel) -> CropCoefficientInput:
        return CropCoefficientInput(
            crop_name=crop_coefficient_model.crop_name,
            crop_type=crop_coefficient_model.crop_type,
            kc_initial=crop_coefficient_model.kc_initial,
            kc_mid_season=crop_coefficient_model.kc_mid_season,
            kc_final=crop_coefficient_model.kc_final,
        )
