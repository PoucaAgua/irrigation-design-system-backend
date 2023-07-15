from typing import Optional

from sqlalchemy.orm import Session

from core.domain.entity.project_entity import ProjectEntity
from infrastructure.persistence.mappers.project import ProjectMapper
from infrastructure.persistence.models import Project


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def upsert(self, project_entity: ProjectEntity):
        project_db = ProjectMapper.entity_to_model(project_entity)
        if project_db.id is None:
            self.db.add(project_db)
        else:
            self.db.merge(project_db)
        self.db.commit()

    def get_by_id(self, _id: int) -> Optional[Project]:
        return self.db.query(Project).filter(Project.id == _id).first()

    def getAll(self):
        pass
