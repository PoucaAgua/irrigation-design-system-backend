from core.domain.entity.project_entity import ProjectEntity
from infrastructure.persistence.repository.projects_repository import ProjectRepository


class ProjectService:

    def __init__(self, repository):
        self.repository = repository

    def upsert_project(self, entity: ProjectEntity):
        self.repository.upsert(entity)
