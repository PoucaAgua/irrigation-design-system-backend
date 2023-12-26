from core.domain.entity.crop_coefficient_input import (
    CropCoefficientInput,
)
from infrastructure.persistence.models.crop_coefficient import (
    CropCoefficientModel,
)


class CropCoefficientMapper:
    @staticmethod
    def entity_to_model(crop_coefficient_input: CropCoefficientInput) -> CropCoefficientModel:
        field_mappings = dict(
            id=crop_coefficient_input.id,
            crop_name=crop_coefficient_input.crop_name,
            crop_type=crop_coefficient_input.crop_type,
            kc_initial=crop_coefficient_input.kc_initial,
            kc_mid_season=crop_coefficient_input.kc_mid_season,
            kc_final=crop_coefficient_input.kc_final,
            active=crop_coefficient_input.active,
        )

        return CropCoefficientModel(**field_mappings)

    @staticmethod
    def entity_to_model_persisted(
        entity_input: CropCoefficientInput, persisted: CropCoefficientModel
    ) -> CropCoefficientModel:
        field_mappings = {
            "id": entity_input.id,
            "crop_name": entity_input.crop_name or persisted.crop_name,
            "crop_type": entity_input.crop_type or persisted.crop_type,
            "kc_initial": entity_input.kc_initial
            if entity_input.kc_initial is not None
            else persisted.kc_initial,
            "kc_mid_season": entity_input.kc_mid_season
            if entity_input.kc_mid_season is not None
            else persisted.kc_mid_season,
            "kc_final": entity_input.kc_final
            if entity_input.kc_final is not None
            else persisted.kc_final,
            "active": entity_input.active if entity_input.active is not None else persisted.active,
        }

        updated_fields = {
            key: value for key, value in field_mappings.items() if value != getattr(persisted, key)
        }

        if updated_fields:
            return CropCoefficientModel(**updated_fields)
        return persisted
