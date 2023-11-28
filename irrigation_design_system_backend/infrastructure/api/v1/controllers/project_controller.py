from fastapi import APIRouter

from apps.project.project_service import ProjectService
from core.domain.entity.project_input import ProjectInput
from infrastructure.api.v1.responses.project import ProjectResponse

router = APIRouter()


@router.post("/projects", response_model=ProjectResponse)
def projects(project_entity: ProjectInput):
    ProjectService.upsert_project(project_entity)
    return ProjectResponse()


@router.get("", response_model=None)
def find_all():
    return ProjectService.find_all()
