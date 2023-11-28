from core.domain.entity.project_input import ProjectInput
from infrastructure.persistence.repository.projects_repository import (
    ProjectRepository,
)


class ProjectService:
    repository = ProjectRepository()

    @classmethod
    def upsert_project(cls, project_input: ProjectInput):
        cls.repository.upsert(project_input)

    @classmethod
    def find_all(cls, group_id: str, user_id: int):
        cls.repository.find_all(group_id, user_id)
