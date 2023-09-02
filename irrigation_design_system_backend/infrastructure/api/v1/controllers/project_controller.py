from fastapi import APIRouter

from apps.project.project_service import ProjectService, DerivationLineService, LateralLineService
from core.domain.entity.project_entity import ProjectEntity, DerivationLineEntity, LateralLineEntity
from infrastructure.api.v1.responses.project import ProjectResponse

router = APIRouter()


@router.post("/projects", response_model=ProjectResponse)
def projects(project_entity: ProjectEntity):
    ProjectService.upsert_project(project_entity)
    return ProjectResponse()


@router.post("/derivation_line", response_model=ProjectResponse)
def derivation(derivation_entity: DerivationLineEntity):
    DerivationLineService.upsert_derivation_line(derivation_entity)
    return ProjectResponse()


@router.post("/lateral_line", response_model=ProjectResponse)
def lateral_line(lateral_line_entity: LateralLineEntity):
    LateralLineService.upsert_lateral_line(lateral_line_entity)
    return ProjectResponse()
