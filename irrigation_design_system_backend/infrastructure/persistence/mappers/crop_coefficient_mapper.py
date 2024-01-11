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

    @classmethod
    def entity_to_model_persisted(
        cls, entity_input: CropCoefficientInput, persisted: CropCoefficientModel
    ) -> CropCoefficientModel:
        model = cls.entity_to_model(entity_input)
        cls.update_model_from_entity(model, entity_input)
        return model

    @staticmethod
    def to_response(model: CropCoefficientModel):
        return model.to_response()
