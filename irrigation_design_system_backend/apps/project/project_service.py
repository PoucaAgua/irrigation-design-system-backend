from core.domain.entity.project_input import ProjectInput, DerivationLineInput, LateralLineInput
from infrastructure.persistence.repository.projects_repository import (
    ProjectRepository,
    DerivationLineRepository,
)
from infrastructure.persistence.repository.projects_repository import LateralLineRepository


class ProjectService:
    repository = ProjectRepository()

    @classmethod
    def upsert_project(cls, entity: ProjectInput):
        cls.repository.upsert(entity)


class DerivationLineService:
    repository = DerivationLineRepository()

    @classmethod
    def upsert_derivation_line(cls, entity: DerivationLineInput):
        cls.repository.upsert(entity)


class LateralLineService:
    repository = LateralLineRepository()

    @classmethod
    def upsert_lateral_line(cls, entity: LateralLineInput):
        cls.repository.upsert(entity)
