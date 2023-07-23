from fastapi import APIRouter

from apps.project.project_service import ProjectService
from core.domain.entity.project_entity import ProjectEntity
from infrastructure.api.v1.responses.project import ProjectResponse
from infrastructure.persistence.repository.projects_repository import ProjectRepository

router = APIRouter()


@router.post("/projects", response_model=ProjectResponse)
def projects(project_entity: ProjectEntity):
    ProjectService.upsert_project(project_entity)
    return ProjectResponse()
