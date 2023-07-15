from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.project.project_service import ProjectService
from core.domain.entity.project_entity import ProjectEntity
from infrastructure.api.v1.responses.project import ProjectResponse
from infrastructure.persistence.repository.projects_repository import ProjectRepository
from infrastructure.persistence.session import get_db

router = APIRouter()


@router.post("/projects", response_model=ProjectResponse)
def projects(project_entity: ProjectEntity, db: Session = Depends(get_db)):
    repository = ProjectRepository(db)
    ProjectService(repository).upsert_project(project_entity)
    return ProjectResponse()
