import pytest
from unittest.mock import Mock, patch

from infrastructure.persistence.repository.projects_repository import ProjectRepository


class TestProjectRepository:

    repository = ProjectRepository()

    @pytest.fixture
    def db(self):
        return Mock()

    @patch('infrastructure.persistence.repository.projects_repository.ProjectMapper')
    def test_upsert_insert(self, project_mapper_mock, db):
        # given
        project_input = Mock()
        project_db_mock = Mock(id=None)
        project_mapper_mock.model_from_input.return_value = project_db_mock

        # when
        result = self.repository.upsert(db=db, project_input=project_input)

        # then
        assert project_db_mock == result
        project_mapper_mock.model_from_input.assert_called_with(project_input)
        db.add.assert_called_with(project_db_mock)
        db.commit.assert_called_once()
        db.close.assert_called_once()

    @patch('infrastructure.persistence.repository.projects_repository.ProjectMapper')
    def test_upsert_update(self, project_mapper_mock, db):
        # given
        project_input = Mock()
        project_db_mock = Mock(id=1)
        project_db_persisted_mock = Mock(id=1)
        project_db_mock_2 = Mock(id=1)

        project_mapper_mock.model_from_input.return_value = project_db_mock
        db.query().filter().first.return_value = project_db_persisted_mock
        project_mapper_mock.model_from_input_and_persisted.return_value = project_db_mock_2

        # when
        result = self.repository.upsert(db=db, project_input=project_input)

        # then
        project_mapper_mock.model_from_input.assert_called_once_with(project_input)
        project_mapper_mock.model_from_input_and_persisted.assert_called_once_with(
            project_input, project_db_persisted_mock
        )

        db.merge.assert_called_with(project_db_mock_2)
        db.commit.assert_called_once()
        db.close.assert_called_once()
