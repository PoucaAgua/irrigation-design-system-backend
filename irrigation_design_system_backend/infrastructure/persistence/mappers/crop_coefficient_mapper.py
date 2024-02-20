from core.domain.entity.crop_coefficient.crop_coefficient_input import CropCoefficientInput
from infrastructure.persistence.models.crop_coefficient_model import CropCoefficientModel


class CropCoefficientMapper:
    @staticmethod
    def entity_to_model(crop_coefficient_input: CropCoefficientInput) -> CropCoefficientModel:
        return CropCoefficientModel(**crop_coefficient_input.dict())

    @staticmethod
    def update_model_from_entity(model: CropCoefficientModel, entity_input: CropCoefficientInput):
        for field, value in entity_input.dict().items():
            if value is not None:
                setattr(model, field, value)

    @staticmethod
    def entity_to_model_persisted(
        entity_input: CropCoefficientInput, persisted: CropCoefficientModel
    ) -> CropCoefficientModel:
        field_mappings = dict(
            crop_id=entity_input.crop_id or persisted.crop_id,
            crop_name=entity_input.crop_name or persisted.crop_name,
            crop_type=entity_input.crop_type or persisted.crop_type,
            kc_initial=entity_input.kc_initial or persisted.kc_initial,
            kc_mid_season=entity_input.kc_mid_season or persisted.kc_mid_season,
            kc_final=entity_input.kc_final or persisted.kc_final,
            is_active=entity_input.is_active or persisted.is_active,
        )

        return CropCoefficientModel(**field_mappings)

    @staticmethod
    def to_response(model: CropCoefficientModel):
        return model.to_response()
