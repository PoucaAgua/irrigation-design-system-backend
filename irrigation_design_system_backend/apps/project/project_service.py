from core.domain.entity.project_input import ProjectInput
from infrastructure.persistence.repository.project_repository import (
    ProjectRepository,
)


class ProjectService:
    repository = ProjectRepository()

    @classmethod
    def upsert_project(cls, project_input: ProjectInput):
        cls.repository.upsert(project_input)

    @classmethod
    def get_all(cls, group_id: str, user_id: int):
        return cls.repository.get_all(group_id, user_id)
