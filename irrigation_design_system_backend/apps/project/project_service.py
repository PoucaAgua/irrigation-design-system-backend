from core.domain.entity.project_entity import ProjectEntity, DerivationLineEntity, LateralLineEntity
from infrastructure.persistence.repository.projects_repository import ProjectRepository, DerivationLineRepository
from infrastructure.persistence.repository.projects_repository import LateralLineRepository


class ProjectService:
    repository = ProjectRepository()

    @classmethod
    def upsert_project(cls, entity: ProjectEntity):
        cls.repository.upsert(entity)


class DerivationLineService:
    repository = DerivationLineRepository()

    @classmethod
    def upsert_derivation_line(cls, entity: DerivationLineEntity):
        cls.repository.upsert(entity)


class LateralLineService:
    repository = LateralLineRepository()

    @classmethod
    def upsert_lateral_line(cls, entity: LateralLineEntity):
        cls.repository.upsert(entity)
