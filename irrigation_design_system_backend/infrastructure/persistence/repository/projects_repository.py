from typing import Optional, List

from core.domain.entity.project_entity import ProjectEntity, DerivationLineEntity, LateralLineEntity
from infrastructure.persistence.mappers.project import ProjectMapper, DerivationLineMapper, LateralLineMapper
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


class DerivationLineRepository:

    @transactional_session
    def upsert(self, db, derivation: DerivationLineEntity):
        project_db = DerivationLineMapper.entity_to_model(derivation)
        if project_db.id is None:
            db.add(project_db)
        else:
            db.merge(project_db)


class LateralLineRepository:

    @transactional_session
    def upsert(self, db, lateral_line: LateralLineEntity):
        lateral_line_db = LateralLineMapper.entity_to_model(lateral_line)
        if lateral_line_db is None:
            db.add(lateral_line_db)
        else:
            db.merge(lateral_line_db)
