from core.domain.entity.project_entity import ProjectEntity, DerivationLineEntity, LateralLineEntity
from infrastructure.persistence.models import Project, DerivationLine, LateralLine


class ProjectMapper:
    @staticmethod
    def entity_to_model(project_entity: ProjectEntity) -> Project:
         return Project(**project_entity.dict())


class DerivationLineMapper:
    @staticmethod
    def entity_to_model(derivation_entity: DerivationLineEntity) -> DerivationLine:
        return DerivationLine(**derivation_entity.dict())


class LateralLineMapper:

    @staticmethod
    def entity_to_model(lateral_line_entity: LateralLineEntity) -> LateralLine:
        return LateralLine(**lateral_line_entity.dict())
