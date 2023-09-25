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
    def __init__(self):
        self.lateral_line_repository = LineRepository(LateralLine, LateralLineMapper)
        self.derivation_line_repository = LineRepository(DerivationLine, DerivationLineMapper)

    @transactional_session
    def upsert(self, db, project_input: ProjectInput):
        project_db = self.__upsert_project(db, project_input)
        self.__upsert_lateral_lines(db, project_input, project_db)
        self.__upsert_derivation_lines(db, project_input, project_db)

    def __upsert_project(self, db, project_input: ProjectInput) -> Project:
        project_db = ProjectMapper.entity_to_model(project_input)
        if project_db.id is None:
            db.add(project_db)
            return project_db

        project_db_persisted = self.get_by_id(project_db.id)
        if project_db_persisted:
            raise ValueError(f"invalid id {project_db.id}")
        project_db_persisted.update_from_new(project_db)
        db.merge(project_db_persisted)
        return project_db_persisted

    def __upsert_lateral_lines(self, db, project_input, project_db):
        for line in project_input.lateral_line:
            self.lateral_line_repository.upsert(db, line, project_db.id)

    def __upsert_derivation_lines(self, db, project_input, project_db):
        for line in project_input.lateral_line:
            self.derivation_line_repository.upsert(db, line, project_db.id)

    @transactional_session
    def get_by_id(self, db, _id: int) -> Optional[Project]:
        return db.query(Project).filter(Project.id == _id).first()

    @transactional_session
    def get_all(self, db) -> List[Project]:
        return db.query(Project).all()


class LineRepository:
    def __init__(self, line_model, line_mapper):
        self.line_model = line_model
        self.line_mapper = line_mapper

    def upsert(self, db, line_input, project_id):
        line_db = self.line_mapper.entity_to_model(line_input, project_id)
        line_db_persisted = self.get_by_project_id_and_type(db, project_id, line_db.type)
        if line_db_persisted is None:
            db.add(line_db)
        else:
            line_db_persisted.update_from_new(line_db)
            db.merge(line_db_persisted)

    @transactional_session
    def get_by_project_id_and_type(self, db, project_id, line_type):
        return (
            db.query(self.line_model)
            .filter(self.line_model.project_id == project_id, self.line_model.type == line_type)
            .first()
        )
