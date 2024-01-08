from core.domain.entity.project_input import ProjectInput


class ProjectService:

    @classmethod
    def upsert_project(cls, project_input: ProjectInput):
        from infrastructure.persistence.repository.project_repository import ProjectRepository
        return ProjectRepository.upsert(project_input)

    @classmethod
    def get_all(cls, group_id: str, user_id: int):
        from infrastructure.persistence.repository.project_repository import ProjectRepository
        return ProjectRepository.get_all(group_id, user_id)
