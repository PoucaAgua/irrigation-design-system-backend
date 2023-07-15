from core.domain.entity.project_entity import ProjectEntity
from infrastructure.persistence.models import Project


class ProjectMapper:
    @staticmethod
    def entity_to_model(project_entity: ProjectEntity) -> Project:
         return Project(**project_entity.dict())
