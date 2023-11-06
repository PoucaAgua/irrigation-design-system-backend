import pytest
from unittest.mock import Mock, patch

from infrastructure.persistence.mappers.project_mapper import ProjectMapper
from infrastructure.persistence.models.projects import Project
from core.domain.entity.project_input import ProjectInput
from infrastructure.persistence.repository.projects_repository import ProjectRepository


class TestProjectRepository:

    @pytest.fixture
    def db(self):
        return Mock()

    def test_upsert_insert(self, db):

        project_input = ProjectInput(
            id=1,
            user_id="1",
            group_id="1",
            description="Lemon farming",
            status="draft",
            crop="Lemon",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=500,
            derivation_line=[],
            lateral_line=[]
        )
        repository = ProjectRepository()

        repository.upsert(project_input, db=db)

        # Assert that the necessary methods were called
        db.save.assert_called_with(Mock())

