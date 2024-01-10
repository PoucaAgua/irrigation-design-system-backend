from typing import List

from core.domain.entity.project.project_input import ProjectInput
from core.domain.entity.project.project_output import ProjectGetAllOutput
from infrastructure.persistence.repository.project_repository import (
    ProjectRepository,
)


class ProjectService:
    repository = ProjectRepository()

    @classmethod
    def upsert_project(cls, project_input: ProjectInput):
        cls.repository.upsert(project_input)

    @classmethod
    def get_all(cls, group_id: str, user_id: int) -> List[ProjectGetAllOutput]:
        return cls.repository.get_all(group_id, user_id)
