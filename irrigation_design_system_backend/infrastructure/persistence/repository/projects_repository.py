from typing import Optional, List, Any

from core.domain.entity.project_input import ProjectInput
from infrastructure.persistence.mappers.project_mapper import (
    ProjectMapper,
)
from infrastructure.persistence.models import Project
from infrastructure.persistence.session import transactional_session


class ProjectRepository:
    @transactional_session
    def upsert(self, db, project_input: ProjectInput) -> Project:
        project_db = ProjectMapper.model_from_input(project_input)
        if project_db.id is None:
            db.add(project_db)
            return project_db

        project_db_persisted = self.__get_by_id(db, project_db.id)
        if not project_db_persisted:
            raise ValueError(f"invalid id {project_db.id}")

        project_db = ProjectMapper.model_from_input_and_persisted(
            project_input, project_db_persisted
        )
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

    @transactional_session
    def find_all(self, db, group_id: str, user_id: int) -> List[Any]:
        projects = (
            db.query(Project).filter(Project.group_id == group_id, Project.user_id == user_id).all()
        )

        return [ProjectMapper.to_json(project) for project in projects]
