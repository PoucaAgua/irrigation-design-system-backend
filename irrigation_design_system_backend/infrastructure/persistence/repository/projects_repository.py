from typing import Optional, List

from core.domain.entity.project_input import ProjectInput
from infrastructure.persistence.mappers.project_mapper import (
    ProjectMapper,
    DerivationLineMapper,
    LateralLineMapper,
)
from infrastructure.persistence.models import Project, DerivationLine, LateralLine
from infrastructure.persistence.session import transactional_session


class ProjectRepository:
    @transactional_session
    def upsert(self, db, project_input: ProjectInput):
        project_db = ProjectMapper.entity_to_model(project_input)
        if project_db.id is None:
            db.add(project_db)
            return project_db

        project_db_persisted = self.__get_by_id(db, project_db.id)
        if not project_db_persisted:
            raise ValueError(f"invalid id {project_db.id}")

        db.merge(project_db)
        return project_db

    @transactional_session
    def get_by_id(self, db, _id: int) -> Optional[Project]:
        return self.__get_by_id(db, _id)

    @staticmethod
    def __get_by_id(db, _id: int) -> Optional[Project]:
        return db.query(Project).filter(Project.id == _id).first()

    @transactional_session
    def get_all(self, db) -> List[Project]:
        return db.query(Project).all()
