from typing import Optional, List

from core.domain.entity.project_entity import ProjectEntity
from infrastructure.persistence.mappers.project import ProjectMapper
from infrastructure.persistence.models import Project
from infrastructure.persistence.session import transactional_session


class ProjectRepository:

    @transactional_session
    def upsert(self, db, project_entity: ProjectEntity):
        project_db = ProjectMapper.entity_to_model(project_entity)
        if project_db.id is None:
            db.add(project_db)
        else:
            db.merge(project_db)

    @transactional_session
    def get_by_id(self, db, _id: int) -> Optional[Project]:
        return db.query(Project).filter(Project.id == _id).first()

    @transactional_session
    def get_all(self, db) -> List[Project]:
        return db.query(Project).all()

