from fastapi import APIRouter
from typing import List

from apps.project.project_service import ProjectService
from core.domain.entity.project.project_input import ProjectInput
from core.domain.entity.project.project_output import ProjectResponse, ProjectGetAllOutput

router = APIRouter()


@router.post("/projects", response_model=ProjectResponse)
def projects(project_entity: ProjectInput):
    ProjectService.upsert_project(project_entity)
    return ProjectResponse()


@router.get("", response_model=List[ProjectGetAllOutput])
def get_all(group_id: str, user_id: int):
    return ProjectService.get_all(group_id, user_id)
