from core.domain.entity.project_entity import ProjectEntity
from infrastructure.persistence.repository.projects_repository import ProjectRepository


class ProjectService:
    repository = ProjectRepository()

    @classmethod
    def upsert_project(cls, entity: ProjectEntity):
        cls.repository.upsert(entity)
