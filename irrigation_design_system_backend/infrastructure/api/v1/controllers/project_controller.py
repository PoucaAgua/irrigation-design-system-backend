from fastapi import APIRouter
from typing import List

from apps.project.project_service import ProjectService
from core.domain.entity.project_input import ProjectInput
from infrastructure.api.v1.responses.project_response import ProjectResponse, ProjectGetAllResponse

router = APIRouter()


@router.post("/projects", response_model=ProjectResponse)
def projects(project_entity: ProjectInput):
    ProjectService.upsert_project(project_entity)
    return ProjectResponse()


@router.get("", response_model=List[ProjectGetAllResponse])
def get_all(group_id: str, user_id: int):
    projects = ProjectService.get_all(group_id, user_id)

    if not projects:
        return []

    return ProjectGetAllResponse.from_domain(projects)
