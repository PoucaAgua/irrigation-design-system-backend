from core.domain.entity.project_input import ProjectInput
from infrastructure.persistence.repository.projects_repository import (
    ProjectRepository,
)


class ProjectService:
    repository = ProjectRepository()

    @classmethod
    def upsert_project(cls, entity: ProjectInput):
        cls.repository.upsert(entity)
